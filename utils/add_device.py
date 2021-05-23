import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
# import requests
# import os
import time
# from dotenv import load_dotenv
# from jsonDecimals import DecimalEncoder as de
import uuid





def add_device(device_name):

    try:

        attribute_name = 'log_id'
        key_type = 'HASH'
        attribute_type = 'N'
        rcu = 5
        wcu = 5

        dynamodb = boto3.resource('dynamodb')

        uid = uuid.uuid4()
        uid = uuni_id.hex
        table_name = 'device_' + uid


        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': attribute_name,
                    'KeyType': key_type
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': attribute_name,
                    'AttributeType': attribute_type
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': rcu,
                'WriteCapacityUnits': wcu
            }
        )

        # Wait until the table exists.
        table.meta.client.get_waiter('table_exists').wait(TableName=table_name)

        device_list_table = dynamodb.Table('device_list')
        current_time = round(time.time())

        table_list_res = device_list_table.put_item(
            Item = {
                'device_key': table_name,
                'created_at': current_time,
                'device_name': device_name
            }
        )        

        temperature_id = 'temperature_' + uuid.uuid4().hex
        pressure_id = 'pressure_' + uuid.uuid4().hex

        new_device_table = dynamodb.Table(table_name)

        response = new_device_table.put_item(
            Item = {
                'log_id': 'device_info',
                'device_key': device_name,
                'pressure_sensor_id': temperature_id,
                'temperature_sensor_id': pressure_id,
            },
            ConditionExpression='attribute_not_exists(id)',
        )


        # Print out some data about the table.
        print(table.item_count)

        res = 'success'
        return res

    except Exception as e:
        print(e)
        res = 'there was an error in adding the device'

        return res