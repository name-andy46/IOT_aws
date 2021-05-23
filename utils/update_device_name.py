import json
import boto3
from boto3.dynamodb.conditions import Key, Attr


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
            UpdateExpression='SET device_name = :val1',
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
