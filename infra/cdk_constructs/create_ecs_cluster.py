from aws_cdk import aws_ecs as ecs
from aws_cdk import aws_ec2 as ec2
from constructs import Construct

class ECSClusterConstruct(Construct):
    
   def __init__(self, scope: Construct, construct_id: str, *,vpc=ec2.Vpc) -> None:
      super().__init__(scope, construct_id)
      self.cluster=ecs.Cluster(scope,"BookingECS",cluster_name="booking_cluster",vpc=vpc,enable_fargate_capacity_providers=True)