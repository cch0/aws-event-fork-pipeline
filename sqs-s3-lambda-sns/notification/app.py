import json
import boto3
import os

def lambda_handler(event, context):
    print(event)
    print("Received event, numberOfRecords: " + str(len(event['Records'])))

    s3_client = boto3.client('s3')
    sns_client = boto3.client('sns')
    
    s3_bucket_name=os.environ['bucketName']
    sns_topic=os.environ['topicArn']

    for record in event['Records']:
        print('processing record, ' + str(record))
        
        # s3
        object_key = record['s3']['object']['key']
        print('object_key:' + object_key)
        
        response = s3_client.get_object(
            Bucket=s3_bucket_name,
            Key=object_key
            )
        
        # print(response)
        
        body = response['Body'].read().decode('utf-8') 
        # print('content:' + body)
        
        sns_message="message arrive:\n%s" % (body)
        
        sns_client.publish(
            TopicArn=sns_topic,
            Message=sns_message,
            Subject='message arrived'
            )
