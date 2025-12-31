# Practice Test 8

- Score 78%
![PT 8 Results](../media/pt-8-results.png)

# ToDo list review:
- Security
- Refactoring
    - [CF configuring secure access and restricting access to content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecurityAndPrivateContent.html)
- Deployment
- Monitor and Troubleshooting
- Review Development with AWS services

## Review Security
- An application hosted in an Auto Scaling group of On-Demand EC2 instances is used to process data polled from an SQS queue and the generated output is stored in an S3 bucket. To improve security, you were tasked to ensure that all objects in the S3 bucket are encrypted at rest using server-side encryption with AWS KMS–Managed Keys (SSE-KMS). Which of the following is required to properly implement this requirement?
    - Add a bucket policy which denies any s3:PutObject action unless the request includes the x-amz-server-side-encryption header
    - Adding a bucket policy which denies any s3:PutObject action unless the request includes the x-amz-server-side-encryption-aws-kms-key-id header 
    - Adding a bucket policy which denies any s3:PostObject action unless the request includes the x-amz-server-side-encryption header
    - Adding a bucket policy which denies any s3:PostObject action unless the request includes the x-amz-server-side-encryption-aws-kms-key-id header

https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html

https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html

https://tutorialsdojo.com/amazon-s3/

<p align="center">____________________</p>

- You have a private S3 bucket that stores application logs and the bucket contents are accessible to all members of the Developer IAM group. However, you want to make an object inside the bucket which should only be accessible to the members of Admin IAM group. How can you apply an S3 bucket policy to this object using AWS CLI?
    - Use the `put-bucket-policy --policy` command
    - Use the `put-bucket-policy--grants` command
    - Use the `put-bucket-policy --permissions` command
    - None of the above

https://docs.aws.amazon.com/AmazonS3/latest/dev/S3_ACLs_UsingACLs.html

https://docs.aws.amazon.com/cli/latest/reference/s3api/put-bucket-policy.html

https://tutorialsdojo.com/amazon-s3/

## Review Refactoring
- You are managing a distributed system which is composed of an Application Load Balancer, SQS queue, and an Auto Scaling group of EC2 instances. The system has been integrated with CloudFront to better serve their clients around the globe. To improve the security of your in-flight data, you were instructed to establish an end-to-end SSL connection between your origin and your end users. How can you meet this requirement using CloudFront? (Select TWO.)
    - Configuring your ALB to only allow traffic on port 443 using an SSL certificate from AWS Config
    - Configuring the Origin Protocol Policy
    - Setting up an Origin Access Identity (OAI)
    - Configuring Viewer Protocol Policy
    - Associating a Web ACL using AWS WAF with your CloudFront Distribution

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-cloudfront-to-custom-origin.html#using-https-cloudfront-to-origin-certificate

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.html

https://tutorialsdojo.com/amazon-cloudfront/

<p align="center">____________________</p>


- A website is hosted in an Auto Scaling group of EC2 instances behind an Application Load Balancer. It also uses CloudFront with a default domain name to distribute its static assets and dynamic contents. However, the website has a poor search ranking as it doesn't use a secure HTTPS/SSL on its site. Which are the possible solutions that the developer can implement in order to set up HTTPS communication between the viewers and CloudFront? (Select TWO.)
    - Using a self-signed SSL/TLS certificate in the ALB which is stored in a private S3 bucket
    - Viewer Protocol Policy to use Redirect HTTP to HTTPS
    - Configuring the ALB to use its default SSL/TLS certificate
    - Using a self-signed certificate in the ALB
    - Viewer Protocol Policy to use HTTPS Only 

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-cloudfront-to-custom-origin.html#using-https-cloudfront-to-origin-certificate

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.html

https://tutorialsdojo.com/amazon-cloudfront/

<p align="center">____________________</p>

- A developer is working on a photo-sharing application that can automatically add filters to the images uploaded by its users. For every new image that the user uploads, it will be handled by an image processing application hosted in a Lambda function. The processed image would then be stored in an S3 bucket. If the upload was successful, the application will return a prompt telling the user that the upload is successful. However, the entire processing typically takes an average of 5 minutes to complete, which causes the application to become unresponsive. Which of the following is the MOST suitable and cost-effective option which will prevent your application from being unresponsive?
    - Using AWS Serverless Application Model (AWS SAM) to allow asynchronous requests to your Lambda function
    - configure the application to asynchronously process the requests and change the invocation type of the Lambda function to Event.
    - Configuring the application to asynchronously process the requests and use the default invocation type of the Lambda function
    - Using a combination of Lambda and Step Functions to orchestrate service components and asynchronously process the requests 

https://docs.aws.amazon.com/lambda/latest/dg/invocation-options.html

https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html

https://tutorialsdojo.com/aws-lambda/

<p align="center">____________________</p>

- A reporting application is hosted in Elastic Beanstalk and uses DynamoDB as its database. If a user requests for data, it scans the entire table and returns the requested data. In the coming weeks, it is expected that the table will grow due to the surge of new users and requested reports. Which of the following should be done as a preparation to improve the performance of the application with minimal cost? (Select TWO.)
    - Reduce page size
    - Isolate scan operations
    - Using DynamoDB Accelerator (DAX)
    - Increasing page size
    - Increasing the Write Compute Unit (WCU)

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-query-scan.html#bp-query-scan-spikes

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html

https://tutorialsdojo.com/amazon-dynamodb/

## Review Deployment
- You have created a Node.js Lambda function that updates a DynamoDB table and sends an email notification via Amazon SNS. However, upon testing, the function is not working as expected. Which of the following is the BEST way to troubleshoot this issue?
    - AWS CloudTrail 
    - Amazon CloudWatch 
    - AWS X-Ray 
    - Amazon Inspector

https://aws.amazon.com/xray/

https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions-logs.html

https://tutorialsdojo.com/aws-x-ray/

https://tutorialsdojo.com/aws-lambda/

<p align="center">____________________</p>

- An internal web application is hosted in a custom VPC with multiple private subnets only. Every EC2 instance that will be provisioned on this VPC will require access to an S3 bucket to pull configuration files as well as to push application logs. Which of the following options is the most suitable solution to use in this scenario?
    - S3 is not part of your VPC
    - Use the AWS SDK for your application and issue the aws configure CLI command to store your access keys, which will be referred to by the SDK
    - Create an IAM Role and attach it to each EC2 instance
    - Store the IAM user and password in the application code to access the S3 bucket

https://aws.amazon.com/blogs/aws/new-vpc-endpoint-for-amazon-s3

https://aws.amazon.com/premiumsupport/knowledge-center/connect-s3-vpc-endpoint/

https://tutorialsdojo.com/amazon-vpc/

<p align="center">____________________</p>

- An internal web application is hosted in a custom VPC with multiple private subnets only. Every EC2 instance that will be provisioned on this VPC will require access to an S3 bucket to pull configuration files as well as to push application logs. Which of the following options is the most suitable solution to use in this scenario?
    - Use the AWS SDK for your application and issue the aws configure CLI command to store your access keys, which will be referred to by the SDK
    - Create an IAM Role and attach it to each EC2 instance
    - Store the IAM user and password in the application code to access the S3 bucket
    - Creating a VPC endpoint for S3

https://aws.amazon.com/blogs/aws/new-vpc-endpoint-for-amazon-s3

https://aws.amazon.com/premiumsupport/knowledge-center/connect-s3-vpc-endpoint/

<p align="center">____________________</p>

- A developer is building an e-commerce application which will be hosted in an ECS Cluster. To minimize the number of instances in use, she must select a strategy which will place tasks based on the least available amount of CPU or memory. Which of the following task placement strategy should the developer implement?
    - binpack
    - random
    - spread
    - distinctInstance

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement.html

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html

https://aws.amazon.com/blogs/compute/amazon-ecs-task-placement/

https://tutorialsdojo.com/amazon-elastic-container-service-amazon-ecs/

## Review Monitor and Troubleshooting
- A mission-critical application is required to have a monitoring system which can provide immediate insight into its sub-minute activity. You are required to collect the data of all of the users who are currently logged in to the system every 10 seconds. Which of the following options is the MOST suitable solution that you should do to meet the above requirements?
    - Publish a high-resolution custom metric to CloudWatch.
    - Publish a custom metric to CloudWatch using the PutMetricData API with the --storage-resolution parameter set to its default value 
    - Enable detailed monitoring
    - Enable enhanced monitoring

https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html

https://aws.amazon.com/premiumsupport/knowledge-center/cloudwatch-custom-metrics/

https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/put-metric-data.html

https://www.youtube.com/watch?v=q0DmxfyGkeU

https://tutorialsdojo.com/amazon-cloudwatch/


<p align="center">____________________</p>

- A developer configured an Amazon API Gateway proxy integration named MyAPI to work with a Lambda function. However, when the API is being called, the developer receives a 502 Bad Gateway error. She tried invoking the underlying function but it properly returns the result in XML format. What is the MOST likely root cause of this issue?
    - The API name of the Amazon API Gateway proxy is invalid
    - There has been an occasional out-of-order invocation due to heavy loads
    - The endpoint request timed-out
    - There is an incompatible output returned from a Lambda proxy integration backend.

https://aws.amazon.com/premiumsupport/knowledge-center/malformed-502-api-gateway/

https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-output-format

https://docs.aws.amazon.com/apigateway/api-reference/handling-errors/

https://tutorialsdojo.com/amazon-api-gateway/

<p align="center">____________________</p>

- A recently deployed Lambda function has an intermittent issue in processing customer data. You enabled the active tracing option in order to detect, analyze, and optimize performance issues of your function using the X-Ray service. Which of the following environment variables are used by AWS Lambda to facilitate communication with X-Ray? (Select TWO.)
    - _X_AMZN_TRACE_ID
    - AWS_XRAY_CONTEXT_MISSING
    - AWS_XRAY_TRACING_NAME
    - AWS_XRAY_DEBUG_MODE
    - AUTO_INSTRUMENT

https://docs.aws.amazon.com/lambda/latest/dg/lambda-x-ray.html#viewing-lambda-xray-results

https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-nodejs-configuration.html

https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python-configuration.html

https://tutorialsdojo.com/aws-x-ray/

https://tutorialsdojo.com/instrumenting-your-application-with-aws-x-ray/

<p align="center">____________________</p>

- A serverless application, which is composed of Lambda functions integrated with API Gateway and DynamoDB, processes ad hoc requests that are sent by its users. Due to the recent spike in incoming traffic, some of your customers are complaining that they are getting HTTP 504 errors from time to time. Which of the following is the MOST likely cause of this issue?
    - An authorization failure occurred between API Gateway and the Lambda function
    - The usage plan quota has been exceeded for the Lambda function
    - Since the incoming requests are increasing, the API Gateway automatically enabled throttling which caused the HTTP 504 errors.
    - API Gateway request has timed out because the underlying Lambda function has been running for more than 29 seconds. 

https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html

https://aws.amazon.com/about-aws/whats-new/2017/11/customize-integration-timeouts-in-amazon-api-gateway/

https://docs.aws.amazon.com/apigateway/latest/developerguide/supported-gateway-response-types.html

https://tutorialsdojo.com/amazon-api-gateway/

<p align="center">____________________</p>

- A Software Engineer is refactoring a Lambda function, which currently uses a public GraphQL API from the Internet as part of its processing. The new requirement states that the function should process the data and store the results to a database hosted in your VPC. The additional VPC-specific information has already been configured in the function and the database connection has been successfully established. However, after testing, he found that the function can't connect to the Internet anymore. Which of the following should the Software Engineer do to fix this issue? (Select TWO.)
    - Configuring your function to forward payloads that were not processed to a dead-letter queue (DLQ) using Amazon SQS
    - Add a NAT gateway to your VPC
    - Submitting a limit increase request to AWS to raise the concurrent executions limit of your Lambda function
    - Ensure that the associated security group of the Lambda function allows outbound connections.
    - Setting up elastic network interfaces (ENIs) to enable your Lambda function to connect securely to other resources within your private VPC 

https://docs.aws.amazon.com/lambda/latest/dg/vpc.html

https://aws.amazon.com/premiumsupport/knowledge-center/internet-access-lambda-function/

https://tutorialsdojo.com/aws-lambda/

## Review Development with AWS services
- There has been reports that your application, which has a MySQL RDS database, becomes unresponsive from time to time. You were instructed to collect all SQL statements that took longer to execute for troubleshooting. What should you do to properly troubleshoot this issue with the LEAST amount of effort?
    - Instrumenting your application using the X-Ray SDK
    - Enabling active tracing using AWS X-Ray
    - Using Amazon Inspector to get all the slow queries 
    - Enabling the slow query log in RDS

https://aws.amazon.com/blogs/database/monitor-amazon-rds-for-mysql-and-mariadb-logs-with-amazon-cloudwatch/

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.MySQL.html

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html

https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/

<p align="center">____________________</p>

- A web application is running in an ECS Cluster and updates data in DynamoDB several times a day. The clients retrieve data directly from the DynamoDB through APIs exposed by Amazon API Gateway. Although API caching is enabled, there are specific clients that want to retrieve the latest data from DynamoDB for every API request sent. What should be done to only allow authorized clients to invalidate an API Gateway cache entry when submitting API requests? (Select TWO.)
    - Instructing the client to send a request which contains the Cache-Control: max-age=1 header
    - Providing your clients an authorization token from STS to query data directly from DynamoDB
    - Tick the Require Authorization checkbox in the Cache Settings of your API via the console and instruct the client to send a request which contains the Cache-Control: max-age=0 header. 
    - Modifying the cache settings to retrieve the latest data from DynamoDB if the request header's authorization signature matches your API's trusted clients list 

https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html#invalidate-method-caching

https://aws.amazon.com/api-gateway/faqs/#Throttling_and_Caching

https://tutorialsdojo.com/amazon-api-gateway/

<p align="center">____________________</p>

- A website hosted in AWS has a custom CloudWatch metric to track all HTTP server errors in the site every minute, which occurs intermittently. An existing CloudWatch Alarm has already been configured for this metric but you would like to re-configure this to properly monitor the application. The alarm should only be triggered when all three data points in the most recent three consecutive periods are above the threshold. Which of the following options is the MOST appropriate way to monitor the website based on the given threshold?
    - Set both the Period and Datapoints to Alarm to 3
    - Use high-resolution metrics
    - Set both the Evaluation Period and Datapoints to Alarm to 3
    - Use metric math in CloudWatch to properly compute the threshold

https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html

https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ConsoleAlarms.html

https://tutorialsdojo.com/amazon-cloudwatch/

<p align="center">____________________</p>

- A developer is working on a Lambda function which has an event source mapping to process requests from API Gateway. The function will consistently have 10 requests per second and it will take a maximum of 50 seconds to complete each request. What should the developer do to prevent the function from throttling?
    - Submitting a Service Limit Increase request to AWS to raise your concurrent executions limit
    - Using Dead Letter Queues (DLQ) to reprocess failed requests
    - Implementing traffic shifting in Lambda using Aliases
    - Do nothing since Lambda will automatically scale to handle the load.

https://docs.aws.amazon.com/lambda/latest/dg/running-lambda-code.html

https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html#function-configuration

https://tutorialsdojo.com/aws-lambda/