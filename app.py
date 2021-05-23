import json
import boto3
import requests
import os
from datetime import datetime
from dotenv import load_dotenv
from utils.jsonDecimals import DecimalEncoder as de
from device import *



dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table('devices')
table = dynamodb.Table('device_list')




def handler(event, context):

    try:
        if event['httpMethod'] == 'GET':
            device_action = event['queryStringParameters']['device_action']
            
            if device_action == 'list':
                Items = list_devices()

                return {
                    'statusCode': 200,
                    'body': json.dumps(Items, sort_keys=True, indent=4)
                }
            else:
                res = 'action not recognized'
                return {
                    'statusCode': 404,
                    'body': json.dumps(res)
                }


        else:
            res = 'httpMethod not recognized!'
        
        
            return {
                'statusCode': 200,
                'body': json.dumps(res)
            }
    except Exception as e:
        print(e)
        res = 'there was an error in handling your request'
        return {
            'statusCode': 400,
            'body': json.dumps(res)
        }























# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table('device_list')

# def handler(event, context):
    
#     response = table.scan(
#         AttributesToGet=['device_key', 'created_at', 'name',]
#     )

    
#     Items = []

#     for i in response['Items']:
#         temp_dict = {}

#         temp_dict['device_key'] = i['device_key']
#         temp_dict['name'] = i['name']
#         temp_dict['created_at'] = de().encode(i['created_at'])
#         Items.append(temp_dict)
    
    
#     return {
#         'statusCode': 200,
#         'body': json.dumps(Items, sort_keys=True, indent=4)
#     }


