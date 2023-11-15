import json


def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
    except:
        return {
            "statusCode": 400,
            "body": json.dumps({'message': 'Unable to parse hasura event'})
        }

    message = 'Not able to process request'
    data = body['event']['data']

    if body['table']['name'] == 'notes' and body['event']['op'] == 'INSERT':
        message = f"New note {data['new']['id']} inserted, with data: {data['new']['note']}"

    elif body['table']['name'] == 'notes' and body['event']['op'] == 'UPDATE':
        message = f"Note {data['new']['id']} updated, with data: {data['new']['note']}"

    elif body['table'] == 'notes' and body['event']['op'] == 'DELETE':
        message = f"Note {data['old']['id']} deleted, with data: {data['old']['note']}"
    return {
        "statusCode": 200,
        "body": json.dumps({'message': message})
    }
