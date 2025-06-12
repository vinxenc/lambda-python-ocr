from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as lambda_,
    aws_apigateway as apigw,
)
from constructs import Construct
import os

class LambdaPythonOcrStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define the Lambda function using container image
        fastapi_lambda = lambda_.DockerImageFunction(
            self, "FastApiLambda",
            code=lambda_.DockerImageCode.from_image_asset(
                os.path.join(os.path.dirname(os.path.dirname(__file__)), "app/fastapi")
            ),
            memory_size=1024,
            timeout=Duration.seconds(30),
            environment={
                "PYTHONPATH": "/var/task",
                "LOG_LEVEL": "DEBUG"
            },
        )
        
        # Create API Gateway
        api = apigw.LambdaRestApi(
            self, "OcrApi",
            handler=fastapi_lambda,
            proxy=True,
        )
