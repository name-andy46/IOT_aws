import json
import boto3
import requests
import os
from datetime import datetime
from dotenv import load_dotenv
from utils.jsonDecimals import DecimalEncoder as de


dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table('devices')
table = dynamodb.Table('device_list')


# response = table.scan(
#     AttributesToGet=['num_id', 'name']
# )


response = table.scan(
    AttributesToGet=['device_key', 'created_at', 'name',]
)
# print(json.dumps(response['Items']))

Items = []

for i in response['Items']:
    temp_dict = {}

    temp_dict['device_key'] = i['device_key']
    temp_dict['name'] = i['name']
    temp_dict['created_at'] = de().encode(i['created_at'])
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