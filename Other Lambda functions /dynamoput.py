#https://www.youtube.com/watch?v=-8L4OxotXlE

import json
import boto3

dynamodb = boto3.resoruce('dynamodb')
table = dynamodb.Table('planets')

def lambda_handler(event,context):
     table.put_item(
         Item : {                        
          'id' : 'neptune',
          'temp' : 'cold af'
        } 
     )
     response = {
          'message' : 'item updated '
     }

     return {
          'statusCode' : 200,
          'body': response
     }
     
     
