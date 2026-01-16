from aws_cdk import (Stack)
from constructs import Construct
import cdk_constructs
import contracts
class ServiceStack(Stack):
    
    def __init__(self, scope: Construct, construct_id: str,InfraExports:contracts.InfraExports, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        roles=cdk_constructs.ServiceRolesConstruct(self,"BookingServiceRolesConstruct")
        service=cdk_constructs.ServiceConstruct(self,"BookingServiceConstruct",task_role=roles.ecs_task_role,task_execution_role=roles.ecs_task_execution_role,infra_exports=InfraExports)
