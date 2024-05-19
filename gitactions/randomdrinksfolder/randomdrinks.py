import json
import random

def random_drink():
    drinks = ['coffee','tea','beer', 'wine', 'milk', 'chai latte']
    return random.choice(drinks)

def handler(event, contect):
    drink = random_drink()
    message = f"you should drinksome {drink}"

    return {
        'statusCode' : 200,
        'body' : json.dumps({"message" : message , "drink" : drink})

    }