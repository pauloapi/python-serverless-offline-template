import json

def hi(event, context):
    body = {
        "message": "Hi Serverless Offline!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response