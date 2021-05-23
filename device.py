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
        
        # return {
        #     'statusCode': 200,
        #     'body': json.dumps(Items, sort_keys=True, indent=4)
        # }

    except Exception as e:
        print(e)
        return {
            'statusCode': 400,
            'body': json.dumps(e)
        }


