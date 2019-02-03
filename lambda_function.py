import boto3

import os

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):

    try:
        tableName = os.environ["dynamodbTableName"]
        print('List items from table {} '.format(tableName))
        table = dynamodb.Table(tableName)

        result = table.scan()
                
        print('{} items found !'.format(result['Count']))
        
        return result['Items']

    except Exception as e:
        print(e)
        raise e
    