from aws_cdk import aws_ecs as ecs
from constructs import Construct
from aws_cdk import aws_iam as iam
import contracts

class ServiceConstruct(Construct):
    
   def __init__(self, scope: Construct, construct_id: str,task_role=iam.Role,task_execution_role=iam.Role,InfraExports=contracts.InfraExports) -> None:
      super().__init__(scope, construct_id)
      task_definition= ecs.FargateTaskDefinition(scope,"BookingService",cpu=256,memory_mib=512,task_role=task_role,
                     task_execution_role=task_execution_role)
      task_definition.add_container("frontend",image=ecs.ContainerImage.from_ecr_repository(InfraExports.frontend_repo))
      task_definition.add_container("backend",image=ecs.ContainerImage.from_ecr_repository(InfraExports.backend_repo))
      task_definition.add_container("redis",image=ecs.ContainerImage.from_ecr_repository(InfraExports.redis_repo))
      service=ecs.FargateService(self,"FargateService",task_definition=task_definition,desired_count=1,min_healthy_percent=100,cluster=InfraExports.cluster,service_name="BookingService")
      InfraExports.alb_listener.add_targets("BookingServiceTG",targets=[service],target_group_name="BookingServiceTG",priority=1,port=8000,health_check=True)
