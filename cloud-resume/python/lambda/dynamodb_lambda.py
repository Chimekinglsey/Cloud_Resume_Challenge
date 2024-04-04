import boto3
import json

def lambda_handler(event, context):
    # Create a DynamoDB resource
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('resume_visitors')

    # Retrieve the item from DynamoDB
    response = table.get_item(Key={'id': '0'})
    
    # Check if the item exists, if not, initialize the views_count attribute
    if 'Item' not in response:
        views_count = 121
        table.put_item(Item={'id': '0', 'views_count': views_count})
    else:
        # Increment the views_count attribute if the item exists
        views_count = response['Item'].get('views_count', 0) + 1
        table.update_item(
            Key={'id': '0'},
            UpdateExpression='SET views_count = :new_count',
            ExpressionAttributeValues={':new_count': views_count}
        )
    
    return {
        'views': int(views_count)
    }
