from __future__ import print_function
import json
import boto3
import time
import urllib



def lambda_handler(event, context):
    s3= boto3.client('s3')
    sb= event['Records'][0]['s3']['bucket']['name']
    print(sb)
    key = event['Records'][0]['s3']['object']['key']
    tb = 'kishan-bucket-2'
    print(tb)
    cp = {'Bucket':sb,'Key':key}
    try:
       
        s3.copy_object(Bucket=tb,Key=key,CopySource=cp)
    except Exception as e:
        raise e


