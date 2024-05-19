import json
# import random

# def random_drink():
#     drinks = ['coffee','tea','beer', 'wine', 'milk', 'chai latte']
#     return random.choice(drinks)

def handler(event, contect):
    # drink = random_drink()
    # message = f"you should drinksome {drink}"
    response_body = {
        "message" : "Hello World",
        "Version" : "1.0.0"
    }

    return {
        'statusCode' : 200,
        'body' : response_body

    }