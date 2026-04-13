import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('UserLog')

def log_activity(action, user_name="", genre=""):
    try:
        table.put_item(
            Item={
                'activity_id': str(uuid.uuid4()),
                'action': action,
                'user_name': user_name,
                'genre': genre,
                'timestamp': datetime.utcnow().isoformat()
            }
        )
    except Exception as e:
        print("DynamoDB error:", e)


def get_logs():
    try:
        response = table.scan()
        return response.get('Items', [])
    except Exception as e:
        print("DynamoDB read error:", e)
        return []