import json
# import random
import os 

# def random_drink():
#     drinks = ['coffee','tea','beer', 'wine', 'milk', 'chai latte']
#     return random.choice(drinks)

def handler(event, contect):
    # drink = random_drink()
    # message = f"you should drinksome {drink}"
    version = os.environ.get("VERSION", "0.0")
    response_body = {
        "message" : "Hello World this is new version",
        "Version" : version
    }

    return {
        'statusCode' : 200,
        'body' : response_body

    }