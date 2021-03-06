import json
import boto3
# import jsonDecimals

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, D):
            return float(obj)
        return json.JSONEncoder.default(self, obj)


def list_devices():

    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('device_list')
        
        response = table.scan(
            AttributesToGet=['device_key', 'created_at', 'device_name',]
            # AttributesToGet=['device_key', 'device_name']
        )

        
        Items = []

        for i in response['Items']:
            temp_dict = {}

            temp_dict['device_key'] = i['device_key']
            temp_dict['device_name'] = i['device_name']
            # temp_dict['created_at'] = DecimalEncoder().encode(i['created_at'])
            temp_dict['created_at'] = str(i['created_at'])
            Items.append(temp_dict)

        return Items
        

    except Exception as e:
        print(e)
        res = 'error getting device list'
        return res
