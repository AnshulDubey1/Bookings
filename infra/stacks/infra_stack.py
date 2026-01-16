from aws_cdk import (
    Stack
)
from constructs import Construct
import cdk_constructs 
import contracts
class InfraStack(Stack):
    '''
    InfraStack Generates VPC,Security Group,ECR Repositories,ECS Cluster

    Args:
        Stack (_type_): _description_
    '''

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        network=cdk_constructs.NetworkConstruct(scope=self,construct_id="BookingNetworkConstruct")
        sg=cdk_constructs.SGConstruct(scope=self,construct_id="BookingSGConstruct",vpc=network.vpc)
        ecr_frontend=cdk_constructs.ECRConstruct(scope=self,construct_id="BookingECRConstructFrontend",id="BookingFrontend",name="booking_frontend")
        ecr_backend=cdk_constructs.ECRConstruct(scope=self,construct_id="BookingECRConstructBackend",id="BookingBackend",name="booking_backend")
        ecr_redis=cdk_constructs.ECRConstruct(scope=self,construct_id="BookingECRConstructRedis",id="BookingRedis",name="booking_redis")
        ecs_cluster=cdk_constructs.ECSClusterConstruct(scope=self,construct_id="BookingECSClusterConstruct",vpc=network.vpc)
        alb=cdk_constructs.ALBConstruct(self,construct_id="BookingALBConstruct",vpc=network.vpc,alb_sg=sg.alb_sg)
        self.export=contracts.InfraExports(cluster=ecs_cluster.cluster,frontend_repo=ecr_frontend.ecr_repo,backend_repo=ecr_backend.ecr_repo,redis_repo=ecr_redis.ecr_repo,alb_listener=alb.listener)
 
        

 
