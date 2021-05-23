import json
import boto3
import jsonDecimals




def list_devices():

    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('device_list')
        
        response = table.scan(
            AttributesToGet=['device_key', 'created_at', 'device_name',]
        )

        
        Items = []

        for i in response['Items']:
            temp_dict = {}

            temp_dict['device_key'] = i['device_key']
            temp_dict['device_name'] = i['device_name']
            temp_dict['created_at'] = DecimalEncoder().encode(i['created_at'])
            Items.append(temp_dict)

        return Items
        

    except Exception as e:
        print(e)
        res = 'error getting device list'
        return res
