# Deploy a Lambda function using a Lambda function

**ARCHITECTURE**

![image](https://user-images.githubusercontent.com/65907580/161390969-3b3852e9-4126-41e5-b8dc-9aa4ec5fdab9.png)

**NOTE**

1. **deployer-lambda** directory in the repository contains the code for the Lambda function which will be used to deploy another Lambda function.
2. It requires the **role** for the lambda function which has the **permission for both S3 and Lambda**.
3. It also contains **S3 Payload Put Event**.
4. **lambda-code** directory in the repository contains the code of the Lambda function that **needs to be deployed**.
5. It contains a **buildspec.yml** file, which will be used by AWS Codebuild to build the code and store the **artificts** in the **zip format** in an S3 Bucket.
6. This zip file will be fetched by the deployer_lambda function and will deploy the function from the zip file.

**Important Links**
1. [Deploy Lambda using CLI](https://docs.aws.amazon.com/cli/latest/reference/lambda/index.html)
2. [Learn Deploy Lambda function using CLI](https://enlear.academy/deploy-a-lambda-function-using-aws-cloud9-fa9480a58aba?source=your_stories_page----------------------------------------)
3. [AWS Lambda Boto3 Library](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html)

