import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'name':event['name'] 
    }


"""
api = https://g2biiqeup3.execute-api.us-east-1.amazonaws.com/prod
#set($inputRoot = $input.path('$'))
{ "name":"$input.params('name')"}
"""
