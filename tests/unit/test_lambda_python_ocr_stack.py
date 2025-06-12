import aws_cdk as core
import aws_cdk.assertions as assertions

from lambda_python_ocr.lambda_python_ocr_stack import LambdaPythonOcrStack

# example tests. To run these tests, uncomment this file along with the example
# resource in lambda_python_ocr/lambda_python_ocr_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = LambdaPythonOcrStack(app, "lambda-python-ocr")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
