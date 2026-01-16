from aws_cdk import aws_ec2 as ec2
from constructs import Construct

class SGConstruct(Construct):
    '''
    create_sg: Creates two security group one for the load balancer and other for ecs

    Args:
        vpc (aws_ec2.Vpc): Needs a Vpc as a Input in order to create a sg in that vpc

    Returns:
        Two Security Group one for ecs and another for alb
    '''
   
    def __init__(self, scope: Construct, construct_id: str, *,vpc=ec2.Vpc) -> None:
        super().__init__(scope, construct_id)
        ecs_sg=ec2.SecurityGroup(scope,"BookingECSSg",description="Allow inbound access",allow_all_outbound=True,vpc=vpc)

        alb_sg = ec2.SecurityGroup(
        scope,
        "BookingALBSg",
        vpc=vpc,
        description="ALB security group",
        allow_all_outbound=False
        )

        # Ingress: Internet → ALB
        alb_sg.add_ingress_rule(
        peer=ec2.Peer.any_ipv4(),
        connection=ec2.Port.tcp(80),
        description="Allow HTTP from internet"
        )

        alb_sg.add_egress_rule(
        peer=ecs_sg,
        connection=ec2.Port.tcp(80),
        description="Forward traffic to ECS tasks"
        )
        self.ecs_sg=ecs_sg
        self.alb_sg=alb_sg
        