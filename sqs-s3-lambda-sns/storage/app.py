import json
from datetime import datetime
import boto3
import os

def lambda_handler(event, context):    
    # print(event)

    s3_client = boto3.client('s3')
    s3_bucket_name=os.environ['bucketName']
    s3_prefx=os.environ['prefix']
    
    print("Received event, numberOfRecords: " + str(len(event['Records'])))
    
    for record in event['Records']:

        message_body = str(record['body'])
        
        print('processing record, message_body:' + message_body)
        
        timestamp = record['attributes']['SentTimestamp']
        
        date_string = datetime.utcfromtimestamp(int(timestamp)/1000).strftime('%Y/%m/%d')
        # print('date_string:' + date_string)
        
        # filename
        filename = record['messageId']
        
        key = "%s%s/%s" % (s3_prefx, date_string, filename)
        print('key:' + key)
        
        content  = bytes(message_body, 'utf-8')
        
        s3_client.put_object(
            ACL='private',
            Body=content,
            Bucket=s3_bucket_name,
            Key=key)
