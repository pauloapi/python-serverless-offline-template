import json

def hello(event, context):
    body = {
        "message": "Hello Serverless Offline!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response