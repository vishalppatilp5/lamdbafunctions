from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct
from aws_cdk import (
    CfnOutput,
    Stack,
    aws_lambda as _lambda,
    aws_lambda_url as _lambda_url,
    core
)
import os.path
from dotenv import  load_dotenv
load_dotenv()

dirname = os.path.dirname(__file__)
class GitactionsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "GitactionsQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        version = os.getenv('VERSION', '0.0')


        random_drink_function = _lambda.Function(
            self,
            id = "RandomDrinkFunctionV1",
            code= _lambda.Code.from_asset(os.path.join(dirname, 'randomdrinksfolder')),
            handler = "randomdrinks.handler",
            runtime= _lambda.Runtime.PYTHON_3_8,
            environment={
                'VERSION': version
            }
        )

        randondrinksUrl = random_drink_function.add_function_url(
            auth_type=_lambda.FunctionUrlAuthType.NONE,
            cors=_lambda.FunctionUrlCorsOptions(
                # Allow this to be called from websites on https://example.com.
                # Can also be ['*'] to allow all domain.
                allowed_origins= ["*"],
                allowed_methods = [_lambda.HttpMethod.ALL],
                allowed_headers = ['*']
            )
        )

        core.CfnOutput(self, "URL",
            value=randondrinksUrl.url
            )
       

      
