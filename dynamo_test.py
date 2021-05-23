import json
import boto3
import requests
import os
from datetime import datetime
from dotenv import load_dotenv
from utils.jsonDecimals import DecimalEncoder as de


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('devices')


response = table.scan(
    AttributesToGet=['num_id', 'name']
)

Items = []

for i in response['Items']:
    temp_dict = {}

    temp_dict['name'] = i['name']
    # temp_dict['num_id'] = Decimal(i['num_id'])
    temp_dict['num_id'] = de().encode(i['num_id'])
    Items.append(temp_dict)

    # print(i)

# DecimalEncoder().encode({'a': d1+d2})
# print(Items)

# x = json.dumps(Items, sort_keys=True, indent=4)
x = json.dumps(Items)

print(x)







# def handler(event, context):
    
#     response = table.scan(
#         AttributesToGet=['id', 'name',]
#     )
    
    
#     return {
#         'statusCode': 200,
#         'body': json.dumps(response['Items'])
#     }