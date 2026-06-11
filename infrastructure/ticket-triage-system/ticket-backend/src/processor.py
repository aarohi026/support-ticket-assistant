import json

def lambda_handler(event, context):

    for record in event["Records"]:

        ticket = json.loads(
            record["body"]
        )

        print("Processing Ticket")
        print(ticket)

    return {
        "statusCode": 200
    }