import json
import boto3
import os
import uuid

from datetime import datetime

dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table(
    os.environ["TABLE_NAME"]
)

sqs = boto3.client("sqs")

def lambda_handler(event, context):

    body = json.loads(
        event["body"]
    )

    ticket = {

        "ticketId":
            str(uuid.uuid4()),

        "subject":
            body["subject"],

        "description":
            body["description"],

        "status":
            "OPEN",

        "createdAt":
            datetime.utcnow().isoformat()
    }

    table.put_item(
        Item=ticket
    )

    sqs.send_message(

        QueueUrl=
            os.environ["QUEUE_URL"],

        MessageBody=
            json.dumps(ticket)
    )

    return {

        "statusCode": 201,

        "body":
            json.dumps(ticket)
    }