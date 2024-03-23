import boto3
import json

def lambda_handler(event, context):
    # Create a DynamoDB resource
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('visitors')

    if event['httpMethod'] == 'GET':
        # Retrieve the item from DynamoDB
        response = table.get_item(Key={'id': '0'})
        
        # Increment the views_count attribute
        views_count = response.get('Item', {}).get('views_count', 0) + 1
        
        # Update the item in DynamoDB
        table.update_item(
            Key={'id': '0'},  # Ensure you're updating the correct item
            UpdateExpression='SET views_count = :new_count',
            ExpressionAttributeValues={':new_count': views_count}
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({'Total Views': views_count})
        }
