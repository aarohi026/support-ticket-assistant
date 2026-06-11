import json
import boto3
import os

dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table(
    os.environ["TABLE_NAME"]
)

def lambda_handler(event, context):

    response = table.scan()

    items = response["Items"]

    query_params = event.get("queryStringParameters")

    if query_params:

        status = query_params.get("status")
        priority = query_params.get("priority")

        if status:
            items = [
                item for item in items
                if item.get("status", "").upper() == status.upper()
            ]

        if priority:
            items = [
                item for item in items
                if item.get("priority", "").upper() == priority.upper()
            ]

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(items)
    }