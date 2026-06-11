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

    table.delete_item(

        Key={
            "ticketId": ticket_id
        }
    )

    return {
        "statusCode": 200,
        "body": "Deleted"
    }