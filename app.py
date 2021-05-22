import json
import boto3
import requests
import os
from datetime import datetime
from dotenv import load_dotenv


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('devices')


def handler(event, context):
    
    response = table.scan(
        AttributesToGet=['id', 'name',]
    )
    
    
    return {
        'statusCode': 200,
        'body': json.dumps(response['Items'])
    }