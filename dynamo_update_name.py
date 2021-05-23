import json
import boto3

device_name_old = 'device_name-d24b4ef286404e328efa1353814ce26a'
device_list = 'device_list'

dynamodb = boto3.resource('dynamodb')
device_to_be_updated = dynamodb.Table(device_name_old)
devices_table = dynamodb.Table(device_list)



response = device_to_be_updated.get_item(
    Key = {
        'log_id': 'device_info',
    }    
)
print(response['Item'])

table_list_res = devices_table.get_item(
    Key = {
        'device_key': 'ge5g4g54g65h76j88776hh56',
    }    
)
print(table_list_res['Item'])




device_to_be_updated.update_item(
    Key={
        'log_id': 'device_info'
    },
    UpdateExpression='SET device_name = :val1',
    ExpressionAttributeValues={
        ':val1': 'updated device name'
    }
)



updated_response = table.get_item(
    Key = {
        'log_id': 'device_info',
    }    
)
print(updated_response['Item'])

# ge5g4g54g65h76j88776hh56