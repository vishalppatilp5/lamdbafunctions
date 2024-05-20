#get item
#setup a test table in dynamodb

import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('planet')  #table name in dynamodb

def lambda_handler(event,context):
    response = table.get_item(
        key = {'id': 'mercury'}
    )

    return{
        'statusCode' : 200,
        'body' : response
    }