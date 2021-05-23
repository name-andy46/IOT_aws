import json
import boto3
from jsonDecimals import DecimalEncoder as de




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