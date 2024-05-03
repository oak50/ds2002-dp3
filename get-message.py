#!/usr/bin/env python3
import boto3
from botocore.exceptions import ClientError
import requests
import json

url = "https://sqs.us-east-1.amazonaws.com/440848399208/fpt9nh"
sqs = boto3.client('sqs')
def delete_message(handle):
    try:
        # Delete message from SQS queue
        sqs.delete_message(
            QueueUrl=url,
            ReceiptHandle=handle
        )
        print("Message deleted")
    except ClientError as e:
        print(e.response['Error']['Message'])


def get_message():

    gett_message = [] # create list of messages
    sort = [] 
    
    try:
        while len(gett_message)<10:
        # Receive message from SQS queue. Each message has two MessageAttributes: order and word
        # You want to extract these two attributes to reassemble the message
            response = sqs.receive_message(
                QueueUrl=url,
                AttributeNames=['All'],
                MaxNumberOfMessages=1,
                MessageAttributeNames=[
                    'All'
                ]
            )
        # Check if there is a message in the queue or not
            if "Messages" in response:
                gett_message.extend(response['Messages'])
            else:
                print("No message in the queue")

            
        for m in gett_message:
            order = m['MessageAttributes']['order']['StringValue']
            word = m['MessageAttributes']['order']['StringValue']
            
            sort.append({'order': int(order), 'word': word})

        sort = sorted(get_messages, key=lambda x: x['order'])
        sentence = ""
        for item in sort():
            sentence += item['word'] + ' '
        print(sentence)

        for _, _, handle in sorted_messages:
            delete_message(handle)
            
    # Handle errors
    except ClientError as e:
        print(e.response['Error']['Message'])
        exit(1) # exit 

# Trigger the function
if __name__ == "__main__":
    get_message()