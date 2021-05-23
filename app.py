import json
import boto3
import requests
import os
from datetime import datetime
# from dotenv import load_dotenv
# from utils.jsonDecimals import DecimalEncoder as de
from utils.list_devices import list_devices
from utils.update_device_name import update_device_name
from utils.add_device import add_device



dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('device_list')


def handler(event, context):

    try:
        if event['httpMethod'] == 'GET':
            device_action = event['queryStringParameters']['device_action'] if event['queryStringParameters']['device_action'] else None
            
            if device_action == 'list':
                Items = list_devices()
                print('👉 querying list success 👈')
                return {
                    'statusCode': 200,
                    'body': json.dumps(Items, sort_keys=True, indent=4)
                }
            else:
                res = 'action not recognized'
                print('👉 query string param not recognized 👈')
                return {
                    'statusCode': 404,
                    'body': json.dumps(res)
                }

        elif event['httpMethod'] == 'POST':
            auth_stepOne = event['queryStringParameters']['theWord']
            if auth_stepOne != 'there-is-no-such-word':
                res = 'Not Allowed!'
                return {
                    'statusCode': 401,
                    'body': json.dumps(res)
                }
            device_action = event['queryStringParameters']['device_action'] if event['queryStringParameters']['device_action'] else None
            body = json.loads(event['body'])

            if device_action == 'update':
                device_key = body['device_key']
                new_name = body['new_name']
                Item = update_device_name(new_name, device_key)

                print('👉 update name success block 👈')
                return {
                    'statusCode': 200,
                    'body': json.dumps(Item, sort_keys=True, indent=4)
                }
            

            elif device_action == 'add':
                device_name = body['device_name']
                second_word = body['second_word']

                if second_word != 'you-are-still-looking-for-the-word':
                    res = 'Not Allowed!'
                    return {
                        'statusCode': 401,
                        'body': json.dumps(res)
                    }

                Item = add_device(device_name)

                return {
                    'statusCode': 200,
                    'body': json.dumps(Item)
                }


            else:
                res = 'action not recognized'
                print('👉 update name not recognized 👈')
                return {
                    'statusCode': 404,
                    'body': json.dumps(res)
                }


        else:
            res = 'httpMethod not recognized!'
            print('👉 http method not recognized 👈')
        
            return {
                'statusCode': 200,
                'body': json.dumps(res)
            }
    except Exception as e:
        print(e)
        print('❌ complete failure ❌')
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


