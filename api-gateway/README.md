# api-gateway-kinesis-stream


## What is in this repository
This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.


- template.yaml - A template that defines the application's AWS resources.

## Goal
The goal of this application is to create a Rest API Endpoint backed by API Gateway to send events to it. Upon receiving events, API Gateway calls Kinesis Stream's PutRecord API to ingest the events.

The AWS resources are defined in the `template.yaml` file in this project.

## Deploy the application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.


To build and deploy your application for the first time, run the following in your shell:

```bash
sam build
sam package --s3-bucket $S3_BUCKET_NAME
sam deploy --stack-name $STACK_NAME --s3-bucket $S3_BUCKET_NAME --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM
```

The first command will build the source of your application. The second command will package your application to AWS. Thast last command will deploy your application to AWS.


## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name $STACK_NAME
```

