import json
import boto3
from botocore.exceptions import ClientError

lambda_client = boto3.client('lambda')

run_time='python3.9'
role='arn:aws:iam::937726284102:role/lambda-deployer-app-role'
handler='lambda_function.lambda_handler'
timeout=60
memory=256

def lambda_handler(event, context):
    
    # Extract S3-Bucket and S3 Obj-Key from the event
    
    for data in event['Records']:
        bucket_name=data['s3']['bucket']['name']
        obj_key=data['s3']['object']['key']
        
    # The name of the Obj in the S3 will be the name of the Lambda Function
    function_name = obj_key.partition('.')[0]
    
    # Check if the Lambda function exists
    try:
        response = lambda_client.get_function(
            FunctionName=function_name
        )
        
        # Lambda function Exists
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            
            # Updating the code of the Lambda function since the function already exists
            update_lambda(function_name, bucket_name, obj_key)
    
    except ClientError as e:
        print(e.response)
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            
            # Create Lambda Function since the function does not exists
            create_lambda(function_name, bucket_name, obj_key)
        else:
            print("Unknown Error")
            print(e)
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
# Creating a new Lambda Function
def create_lambda(function_name, bucket_name, obj_key):
    
    print("Creating lambda function")
    
    response = lambda_client.create_function(
        FunctionName=function_name,
        Runtime=run_time,
        Role=role,
        Handler=handler,
        Code={
            'S3Bucket': bucket_name,
            'S3Key': obj_key
        },
        Timeout=timeout,
        MemorySize=memory
    )
    print(response)
    print("Lambda function created successfully")
    
# Update the code of the Lamabda Function
def update_lambda(function_name, bucket_name, obj_key):
    response = lambda_client.update_function_code(
        FunctionName=function_name,
        S3Bucket=bucket_name,
        S3Key=obj_key,
    )
    print(response)
    print("Lambda function code updated successfully")