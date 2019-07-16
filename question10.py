from __future__ import print_function # Python 2/3 compatibility
import boto3
from boto3.dynamodb.conditions import Key, Attr
import logging
# setting logging config
logging.basicConfig(filename="question10.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w') 
logger=logging.getLogger()
logger.setLevel(logging.ERROR) 
dynamodb = boto3.resource('dynamodb',region_name='us-east-1')

try:

    table = dynamodb.Table('Games123')
    response = table.query(
        KeyConditionExpression=Key('username').eq('johndoe')
    )
    items = response['Items']
    for i in items:
        print(i['gname'],i['rating'])
except Exception as e:
    logger.error(e) 
    print('error occured please check your code ')

