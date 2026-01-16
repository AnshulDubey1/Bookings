#!/usr/bin/env python3
import os

import aws_cdk as cdk

from stacks.infra_stack import InfraStack
from stacks.service_stack import ServiceStack
import contracts

app = cdk.App()
print("meow")
env=cdk.Environment( region='ap-south-1')
stack_name_infra=app.node.try_get_context("stack_name_infra")
stack_name_service=app.node.try_get_context("stack_name_service")
infra_stack=InfraStack(app,stack_name_infra ,env=env)
service_stack=ServiceStack(app,stack_name_service,env=env,InfraExports=infra_stack.export)
app.synth()
