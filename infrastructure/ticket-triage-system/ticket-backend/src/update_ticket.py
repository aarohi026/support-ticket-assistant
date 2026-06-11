import json
import boto3
import os

dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table(
    os.environ["TABLE_NAME"]
)

def lambda_handler(event, context):

    ticket_id = (
        event["pathParameters"]["id"]
    )

    body = json.loads(
        event["body"]
    )

    table.update_item(

        Key={
            "ticketId": ticket_id
        },

        UpdateExpression=
        "SET subject=:s, description=:d",

        ExpressionAttributeValues={

            ":s":
                body["subject"],

            ":d":
                body["description"]
        }
    )

    return {
        "statusCode": 200,
        "body": "Updated"
    }