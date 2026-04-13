from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigateway
)
from constructs import Construct

class AwsCdkCustomAuthorizerTemplateStack(Stack):
     def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # 1. Define Authorizer Lambda
        auth_fn = _lambda.Function(
            self, 
            "AuthHandler",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="index.lambda_handler",
            code=_lambda.Code.from_asset("authorizer_lambda")
        )

        # 2. Create the Authorizer
        authorizer = apigateway.TokenAuthorizer(
            self, 
            "MyAuthorizer",
            handler=auth_fn
        )

        # 3. Define REST API
        api = apigateway.RestApi(self, "MyRestApi")
        resource = api.root.add_resource("secure-data")

        # 4. Apply Authorizer to Method
        resource.add_method(
            http_method="GET",
            integration=apigateway.MockIntegration(), # Replace with your real integration
            authorizer=authorizer,
            authorization_type=apigateway.AuthorizationType.CUSTOM
        )

        # Define the Lambda function
        my_test_lambda = _lambda.Function(
            self, "MyTestLambda",
            runtime=_lambda.Runtime.PYTHON_3_12, # Use latest supported runtime
            code=_lambda.Code.from_asset("lambdas/test_lambda"), # Path to your lambda directory
            handler="index.lambda_handler" # filename.functionname
        )
