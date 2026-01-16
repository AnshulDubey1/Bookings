from aws_cdk import aws_elasticloadbalancingv2 as alb
from aws_cdk import aws_ec2 as ec2

from constructs import Construct

class ALBConstruct(Construct):
    
   def __init__(self, scope: Construct, construct_id: str, *,vpc=ec2.Vpc,alb_sg=ec2.SecurityGroup) -> None:
      super().__init__(scope, construct_id)
      self._load_balancer= alb.ApplicationLoadBalancer(self,"BookingLoadBalancer",vpc=vpc,load_balancer_name="BookingLB",security_group=alb_sg)
      self.listener = self._load_balancer.add_listener(
            "HttpListener",
            port=80,
            open=True,
        )
        