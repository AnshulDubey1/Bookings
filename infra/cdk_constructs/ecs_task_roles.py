from aws_cdk import aws_iam as iam
from constructs import Construct

class ServiceRolesConstruct(Construct):
    '''
    create_ecs_task_roles _summary_

    Args:
        scope (_type_): _description_

    Returns:
        _type_: _description_
    '''   
    def __init__(self, scope: Construct, construct_id: str) -> None:
        super().__init__(scope, construct_id)
        ecs_task_role=iam.Role(scope,"BookingECSTaskRole",assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com"),description="Assumed by ecs tasks")

        ecs_task_execution_role=iam.Role(scope,"BookingECSTaskExecutionRole",assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com"),description="Assumbed by ecs while creating the task",managed_policies=[iam.ManagedPolicy.from_aws_managed_policy_name( "service-role/AmazonECSTaskExecutionRolePolicy")])
    
        self.ecs_task_role=ecs_task_role
        self.ecs_task_execution_role=ecs_task_execution_role