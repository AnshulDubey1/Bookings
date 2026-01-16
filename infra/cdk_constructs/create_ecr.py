from aws_cdk import aws_ecr as ecr
from constructs import Construct

class ECRConstruct(Construct):
    
   def __init__(self, scope: Construct, construct_id: str, *,id,name) -> None:
      super().__init__(scope, construct_id)
      self.ecr_repo= ecr.Repository(scope,id,repository_name=name)
        