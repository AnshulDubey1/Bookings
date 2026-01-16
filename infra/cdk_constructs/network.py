from aws_cdk import aws_ec2 as ec2
from constructs import Construct

class NetworkConstruct(Construct):
    
   def __init__(self, scope: Construct, construct_id: str) -> None:
      super().__init__(scope, construct_id)
      self.vpc=ec2.Vpc(scope,'BookingVPC',nat_gateways=1,max_azs=2,subnet_configuration=[ec2.SubnetConfiguration(name='BookingSubnet',subnet_type=ec2.SubnetType.PUBLIC,cidr_mask=24)])