import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_cdk_custom_authorizer_template.aws_cdk_custom_authorizer_template_stack import AwsCdkCustomAuthorizerTemplateStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_cdk_custom_authorizer_template/aws_cdk_custom_authorizer_template_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsCdkCustomAuthorizerTemplateStack(app, "aws-cdk-custom-authorizer-template")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
