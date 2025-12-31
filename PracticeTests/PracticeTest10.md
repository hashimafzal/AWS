# Practice Test 2

- Score 76%
![PT 10 Results](../media/pt-10-results.png)

# ToDo list review:
- Security
- Refactoring
- Deployment
- Monitor and Troubleshooting
- Review Development with AWS services


## Review Security
- A company has recently adopted a hybrid cloud architecture to augment their on-premises data center with virtual private clouds (VPCs) in AWS. You were assigned to manage all of the company's cloud infrastructure including the security of their resources using IAM. In this scenario, which of the following are best practices in managing security in AWS? (Select TWO.)
    - Using IAM inline policies to delegate permissions
    - Delete root user access keys
    - Always keeping your AWS account root user access key
    - Granting all the permissions to the resource in order to perform the task without any issues
    - Grant only the permissions required by the resource to perform a task

https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html

https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html

https://tutorialsdojo.com/aws-identity-and-access-management-iam/

<p align="center">____________________</p>

- A developer runs a shell script that uses the AWS CLI to upload a large file to an S3 bucket, which includes an AWS KMS key. An Access Denied error always shows up whenever the developer uploads a file with a size of 100 GB or more. However, when he tried to upload a smaller file with the KMS key, the upload succeeds. Which of the following are possible reasons why this issue is happening? (Select TWO.)
    - The AWS CLI S3 commands perform a multipart upload when the file is large.
    - The developer does not have the kms:Decrypt permission
    - The developer does not have the kms:Encrypt permission
    - The developer's IAM permission has an attached inline policy that restricts him from uploading a file to S3 with a size of 100 GB or more
    - The maximum size that can be encrypted in KMS is only 100 GB

https://aws.amazon.com/premiumsupport/knowledge-center/s3-large-file-encryption-kms-key/

https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html#using-s3-commands-managing-objects

https://tutorialsdojo.com/aws-key-management-service-aws-kms/

https://www.youtube.com/watch?v=-1S-RdeAmMo

<p align="center">____________________</p>

- A company has a static website running in an Auto Scaling group of EC2 instances which they want to convert as a dynamic e-commerce web portal. One of the requirements is to use HTTPS to improve the security of their portal and also improve their search ranking as a reputable and secure site. A developer recently requested an SSL/TLS certificate from a third-party certificate authority (CA) which is ready to be imported to AWS. Which of the following services can the developer use to safely import the SSL/TLS certificate? (Select TWO.)
    - AWS Certificate Manager (ACM) 
    - IAM certificate store
    - A private S3 bucket with versioning enabled
    - Amazon Cognito
    - Cloud Front

https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html

https://aws.amazon.com/certificate-manager/

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-procedures.html#cnames-and-https-uploading-certificates

https://tutorialsdojo.com/aws-certificate-manager/

https://youtu.be/ogVamzF2Dzk

## Review Refactoring
- You have an AWS account, with an ID of 061218980612, which is used by the different departments of your company. You used the AWS CLI command iam create-account-alias --account-alias finance-dept to create a user-friendly identifier for your finance department. Which of the following is a valid sign-in page URL for your AWS account?
    - https://061425453612.signin.aws.amazon.com/console
    - https://finance-dept.aws.amazon.com/console
    - https://finance-dept.signin.aws.amazon.com/console
    - https://finance-dept.aws.signin.amazon.com/console

https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html

https://docs.aws.amazon.com/cli/latest/reference/iam/create-account-alias.html

https://tutorialsdojo.com/aws-identity-and-access-management-iam/

## Review Deployment

## Review Monitor and Troubleshooting
- You were recently hired as a developer for a leading insurance firm in Asia which has a hybrid cloud architecture with AWS. The project that was assigned to you involves setting up a static website using Amazon S3 with a CORS configuration as shown below. Which of the following statements are TRUE with regards to this S3 configuration? (Select TWO.)
    - The request will fail if the x-amz-meta-custom-header header is not included
    - This configuration authorizes the user to perform actions on the S3 bucket
    - All HTTP Methods are allowed
    - It allows a user to view, add, remove or update objects inside the S3 bucket from the domain tutorialsdojo.com
    - This will cause the browser to cache an Amazon S3 response of a preflight OPTIONS request for 1 hour

```xml
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
 <CORSRule>
  <AllowedOrigin>https://tutorialsdojo.com</AllowedOrigin>
  <AllowedMethod>GET</AllowedMethod>
  <AllowedMethod>PUT</AllowedMethod>
  <AllowedMethod>POST</AllowedMethod>
  <AllowedMethod>DELETE</AllowedMethod>
  <AllowedHeader>*</AllowedHeader>
  <ExposeHeader>ETag</ExposeHeader>
  <ExposeHeader>x-amz-meta-custom-header</ExposeHeader>
  <MaxAgeSeconds>3600</MaxAgeSeconds>
 </CORSRule>
</CORSConfiguration>
```

## Review Development with AWS services
- A developer is designing an application which will be hosted in ECS and uses an EC2 launch type. You need to group your container instances by certain attributes such as Availability Zone, instance type, or custom metadata. After you have defined a group of container instances, you will need to customize Amazon ECS to place tasks on container instances based on the group you specified. Which of the following ECS features provides you with expressions that you can use to group container instances by a specific attribute?
    - Task Placement Strategy 
    - Task Placement Constraint 
    - Task Group
    - Cluster Query Language

https://aws.amazon.com/blogs/compute/amazon-ecs-task-placement/

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html

https://tutorialsdojo.com/amazon-elastic-container-service-amazon-ecs/

<p align="center">____________________</p>

- A leading technology company is building a serverless application in AWS using the C++ programming language. The application will use DynamoDB as its data store, Lambda as its compute service, and API Gateway as its API Proxy. You are tasked to handle the deployment of the compute resources to AWS. Which of the following steps should you implement to properly deploy the serverless application?
    - Creating a Lambda function with the C++ code and directly uploading it to AWS 
    - Create a new layer which contains the Custom Runtime for C++ and then launch a Lambda function which uses that runtime
    - Using AWS Serverless Application Model (AWS SAM) to deploy the Lambda function
    - Uploading the deployment package to S3 and then using CloudFormation to deploy Lambda function with a reference to the S3 URL of the package

https://docs.aws.amazon.com/lambda/latest/dg/runtimes-custom.html

https://docs.aws.amazon.com/lambda/latest/dg/runtimes-walkthrough.html

https://tutorialsdojo.com/aws-lambda/

<p align="center">____________________</p>

- A development team has several developers where each of them has a corresponding IAM user. It is your primary responsibility to grant the developers access to CodeCommit to enable them to fully utilize the code repositories on their local computers. Which of the following should you implement to grant access to your developers? (Select TWO.)
    - Enabling Multi-Factor Authentication (MFA) for each IAM User 
    - Generating new SSH keys and associating the private SSH key to each of your developer's IAM user
    - Generating Git credentials in Github
    - Generate HTTPS Git credentials and generate new SSH keys and associate the public SSH key to each of your developer's IAM user 

https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up.html

https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control.html

https://tutorialsdojo.com/aws-codecommit/

<p align="center">____________________</p>