import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
import requests
import os
from datetime import datetime
from dotenv import load_dotenv
from utils.jsonDecimals import DecimalEncoder as de
import uuid


uuni_id = uuid.uuid4()
uid_str = uuni_id.hex
print(uid_str)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('devices')


response = table.scan(
    FilterExpression=Attr('num_id').lt(3)
)

# print(response)

Items = []

for i in response['Items']:
    temp_dict = {}

    temp_dict['name'] = i['name']
    # temp_dict['num_id'] = Decimal(i['num_id'])
    temp_dict['num_id'] = de().encode(i['num_id'])
    Items.append(temp_dict)

# x = json.dumps(Items, sort_keys=True, indent=4)
x = json.dumps(Items)

print(x)

