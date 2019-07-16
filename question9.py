from __future__ import print_function # Python 2/3 compatibility
import boto3
from boto3.dynamodb.conditions import Key, Attr
import logging
# setting logging config
logging.basicConfig(filename="question9.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w') 
logger=logging.getLogger()
logger.setLevel(logging.ERROR) 

#connection to boto3
dynamodb = boto3.resource('dynamodb')

#creating table with schema
try:
    table = dynamodb.create_table(
        TableName='Games123',
        KeySchema=[
            {
                'AttributeName': 'gid',
                'KeyType': 'HASH'  #Partition key
            },
            {
                'AttributeName': 'gname',
                'KeyType': 'RANGE'  #Sort key
            },
            
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'gid',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'gname',
                'AttributeType': 'S'
            },
            

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    table.meta.client.get_waiter('table_exists').wait(TableName='Games123')

    print(table)
    print("Table status:", table.table_status)
except Exception as e:
    logger.error(e) 
    print('error occured please check your code ')


#inserting into table
dynamodb = boto3.client('dynamodb',region_name='us-east-1')
try:
    response = dynamodb.put_item(
        Item={
            'gid': {
                'N': '1',
            },
            'gname': {
                'S': 'footbal',
            },
            'publisher': {
                'S': 'abc',
            },
            'rating': {
                'S': '10',
            },
            'release_date': {
                'S': '2/7/19',
            },
            'genres': {
                'SS': ['rock','pop'],
            },
        },
        ReturnConsumedCapacity='TOTAL',
        TableName='Games123',
    )

    print(response)
except Exception as e:
    logger.error(e) 
    print('error occured please check your code ')
