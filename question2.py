import boto3
import logging
# setting logging config
logging.basicConfig(filename="question2.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w') 
logger=logging.getLogger()
logger.setLevel(logging.ERROR) 
# creating object of s3
s3 = boto3.client('s3')
# downloading q2_version file from kishan-bucket with specific version id
try:
    s3.download_file('kiscan-bucket', 'q2_version', 'q2_version.txt', ExtraArgs={'VersionId': '1Bxsxy3fPWSWbS_QOiXV1ymXQPd4Q6oX'})
except Exception as e:
    logger.error(e) 
    print('error occured please check of bucket or objects exists or not ')
