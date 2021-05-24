import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
# import requests
# import os
import time
# from dotenv import load_dotenv
import uuid
import random
from decimal import Decimal



def log_data(device_key):

    response = {}
    
    try:

        dynamodb = boto3.resource('dynamodb')
        device_table = dynamodb.Table(device_key)
        log_time = round(time.time())

        get_count = device_table.get_item(
            Key = {
                'log_id': 'counter',
            }    
        )

        current_count = str(get_count['Item']['count'])
        
        temperature = round(Decimal(random.uniform(-20, 50)), 2)
        pressure = round(Decimal(random.uniform(930, 1050)), 2)
        current_time = round(time.time())

        response['log_result'] = device_table.put_item(
            Item = {
                'log_id': current_count,
                'temperature': temperature,
                'pressure': pressure,
                'log_time': current_time
            },
            ConditionExpression='attribute_not_exists(log_id)',
        )

        updated_count = int(current_count) + 1
        
        update_count = device_table.put_item(
            Item = {
                'log_id': 'counter',
                'count': updated_count
            }
        )

        response['statusCode'] = 200
        response['body'] = 'successfully logged data'

        return response

    except Exception as e:
        print(e)

        response['statusCode'] = 400
        response['body'] = 'error in logging data'

        return response