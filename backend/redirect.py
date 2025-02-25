import json

def lambda_handler(event, context):
    short_code = event['pathParameters']['shortCode']
    # Placeholder redirect (we’ll connect DynamoDB later)
    original_url = "https://example.com"  # Replace with real lookup later
    return {
        'statusCode': 301,
        'headers': {'Location': original_url}
    }