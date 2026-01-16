from aws_cdk import aws_ecs as ecs
from aws_cdk import aws_iam as iam
from aws_cdk import aws_elasticloadbalancingv2 as alb
from constructs import Construct
import contracts


class ServiceConstruct(Construct):

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        task_role: iam.IRole,
        task_execution_role: iam.IRole,
        infra_exports: contracts.InfraExports,
    ) -> None:
        super().__init__(scope, construct_id)

        task_definition = ecs.FargateTaskDefinition(
            self,
            "BookingTaskDef",
            cpu=256,
            memory_limit_mib=512,
            task_role=task_role,
            execution_role=task_execution_role,

        )

        # Frontend container
        frontend = task_definition.add_container(
            "frontend",
            image=ecs.ContainerImage.from_ecr_repository(
                infra_exports.frontend_repo
            ),
            logging=ecs.LogDrivers.aws_logs(stream_prefix="frontend"),
        )
        frontend.add_port_mappings(
            ecs.PortMapping(container_port=3000,host_port=3000, protocol=ecs.Protocol.TCP)
        )

        # Backend container (ALB targets this)
        backend = task_definition.add_container(
            "backend",
            image=ecs.ContainerImage.from_ecr_repository(
                infra_exports.backend_repo
            ),
            logging=ecs.LogDrivers.aws_logs(stream_prefix="backend"),
        )
        backend.add_port_mappings(
            ecs.PortMapping(container_port=8000, host_port=8000,protocol=ecs.Protocol.TCP)
        )

        # Redis container (internal only)
        redis = task_definition.add_container(
            "redis",
            image=ecs.ContainerImage.from_ecr_repository(
                infra_exports.redis_repo
            ),
            logging=ecs.LogDrivers.aws_logs(stream_prefix="redis"),
        )
        redis.add_port_mappings(
            ecs.PortMapping(container_port=6379,host_port=6379, protocol=ecs.Protocol.TCP)
        )

        service = ecs.FargateService(
            self,
            "FargateService",
            cluster=infra_exports.cluster,
            task_definition=task_definition,
            desired_count=1,
            min_healthy_percent=100,
            service_name="BookingService",
        )

        # ALB → frontend container
        target_group = infra_exports.alb_listener.add_targets(
            "BookingServiceTG",
            targets=[service],
            port=3000,
            priority=1,
            conditions=[alb.ListenerCondition.path_patterns(["booking/*"])],
            protocol=alb.ApplicationProtocol.HTTP,
            target_group_name="BookingServiceTG",
        )

        target_group.configure_health_check(
            enabled=True,
            healthy_http_codes="200-399",
            port="3000",
            path="/booking",
        )
