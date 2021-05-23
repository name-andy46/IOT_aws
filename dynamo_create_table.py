import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
# import requests
# import os
# from datetime import datetime
# from dotenv import load_dotenv
# from utils.jsonDecimals import DecimalEncoder as de
# import uuid



dynamodb = boto3.resource('dynamodb')

table_name = 'myDeviceName_-_pjf94u989t8989g9859859g98984'
attribute_name = 'log_id'
key_type = 'HASH'
attribute_type = 'N'
rcu = 5
wcu = 5

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

# Print out some data about the table.
print(table.item_count)