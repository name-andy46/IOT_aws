import json
import boto3
import requests
import os
from datetime import datetime
# from dotenv import load_dotenv
# from utils.jsonDecimals import DecimalEncoder as de
from utils.list_devices import list_devices
from utils.update_device_name import update_device_name
from utils.add_device import add_device, handleDBevent
from utils.logging import log_data



def handler(event, context):
    
    try:
        if 'Records' in event:

            event_record = event['Records'][0]
            res = handleDBevent(event_record)

            if res == 'error':
                print('could not create table')
                return

            if res == 'success':
                print('successfully created table')
                return

        elif event['httpMethod'] == 'GET':
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

            if auth_stepOne != os.environ['authStepOne']:
                res = 'Not Allowed!'
                return {
                    'statusCode': 401,
                    'body': json.dumps(res)
                }

            
            body = json.loads(event['body'])

            auth_stepTwo = body['second_word']

            if auth_stepTwo != os.environ['authStepTwo']:

                res = 'Not Allowed!'

                return {
                    'statusCode': 401,
                    'body': json.dumps(res)
                }

            device_action = event['queryStringParameters']['device_action'] if event['queryStringParameters']['device_action'] else None

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
                
                add_device_response = add_device(device_name)

                return {
                    'statusCode': 200,
                    'body': json.dumps(add_device_response)
                    }



            elif device_action == 'log':

                device_key = body['device_key']

                log_result = log_data(device_key)

                return {
                    'statusCode': log_result['statusCode'],
                    'body': json.dumps(log_result['body'])
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
        



