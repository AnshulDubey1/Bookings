from dataclasses import dataclass
from aws_cdk import aws_ecs as ecs, aws_ecr as ecr,aws_elasticloadbalancingv2 as alb

@dataclass(frozen=True)
class InfraExports:
    cluster: ecs.Cluster
    frontend_repo: ecr.Repository
    backend_repo: ecr.Repository
    redis_repo: ecr.Repository
    alb_listener:alb.ApplicationListener
