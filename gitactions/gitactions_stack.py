
from constructs import Construct
from aws_cdk import (
    CfnOutput,
    Stack,
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb

)
import os.path
import aws_cdk as core

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

        table = dynamodb.TableV2(self, "VisitorTimeTable",
        partition_key=dynamodb.Attribute(name="key", type=dynamodb.AttributeType.STRING),
        billing=dynamodb.Billing.on_demand()
)


        random_drink_function = _lambda.Function(
            self,
            id = "RandomDrinkFunctionV1",
            code= _lambda.Code.from_asset(os.path.join(dirname, 'randomdrinksfolder')),
            handler = "randomdrinks.handler",
            runtime= _lambda.Runtime.PYTHON_3_8,
            environment={
                'VERSION': version,
                'TABLE_NAME': table.table_name,
            }
        )

        table.grant_read_write_data(random_drink_function)

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
       

      
