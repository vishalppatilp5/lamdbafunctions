import json
# import random
import os 
import boto3

# def random_drink():
#     drinks = ['coffee','tea','beer', 'wine', 'milk', 'chai latte']
#     return random.choice(drinks)

def handler(event, contect):
    # drink = random_drink()
    # message = f"you should drinksome {drink}"
    
    path = event["rawPath"]
    if path != "/":
        return {"statusCode": 400 , "body": "Not Found"}

    dynamodb = boto3.resoruce('dynamodb')
    table = dynamodb.Table(os.envron.get("TABLE_NAME"))
    

    response = table.get_item(key={"key": "visit_count"})
    if "Item" in response:
        visit_count = response ["Item" ] ["value"]
    else:
        visit_count = 0

    new_visit_count = visit_count + 1
    table.put_item(Item={"key": "visit_count", "value" : new_visit_count})

    version = os.environ.get("VERSION", "0.0")
    response_body = {
        "message" : "Hello World this is new version",
        "Version" : version,
        "visit_count" : new_visit_count,
    }

    return {
        'statusCode' : 200,
        'body' : response_body

    }