import json
import boto3
# import requests
# import os
# from datetime import datetime
# from dotenv import load_dotenv
from utils.jsonDecimals import DecimalEncoder as de




def list_devices():

    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('device_list')
        
        response = table.scan(
            AttributesToGet=['device_key', 'created_at', 'name',]
        )

        
        Items = []

        for i in response['Items']:
            temp_dict = {}

            temp_dict['device_key'] = i['device_key']
            temp_dict['name'] = i['name']
            temp_dict['created_at'] = de().encode(i['created_at'])
            Items.append(temp_dict)

        return Items
        

    except Exception as e:
        print(e)
        res = 'error getting device list'
        return res



def update_device_name(new_name, device_key):

    try:
        dynamodb = boto3.resource('dynamodb')

        device_to_be_updated = dynamodb.Table(device_key)   # Getting device table to update it's name in the table
        devices_list = dynamodb.Table('device_list')        # Getting devices table list to update the name alongside its key

        device_to_be_updated.update_item(
            Key={
                'log_id': 'device_info'
            },
            UpdateExpression='SET device_name = :val1',
            ExpressionAttributeValues={
                ':val1': new_name
            }
        )

        devices_list.update_item(
            Key={
                'device_key': device_key
            },
            UpdateExpression='SET name = :val1',
            ExpressionAttributeValues={
                ':val1': new_name
            }
        )

        response = device_to_be_updated.get_item(
            Key = {
                'log_id': 'device_info',
            }    
        )

        Item = response['Item']
        return Item

    except Exception as e:
        print(e)
        res = 'error updating the device name'
        return res
