import json
import random
import string

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def lambda_handler(event, context):
    body = json.loads(event['body'])
    original_url = body['url']
    short_code = generate_short_code()
    short_url = f"https://kcxdntjgu5.execute-api.us-west-2.amazonaws.com/prodhttps://kcxdntjgu5.execute-api.us-west-2.amazonaws.com/prod/{short_code}"  # Placeholder URL
    return {
        'statusCode': 200,
        'body': json.dumps({'shortUrl': short_url}),
        'headers': {'Content-Type': 'application/json'}
    }