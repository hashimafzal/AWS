# Practice Test 9

- Score 80%
![PT 9 Results](../media/pt-9-results.png)

# ToDo list review:
- Security
    - GetSessionToken vs Assume Role
- Refactoring
- Deployment
- Monitor and Troubleshooting
    - Deep dive into XRay
- Review Development with AWS services
    - EB cli commands

## Review Security
- A developer is using API Gateway Lambda Authorizer to provide authentication for every API request and control access to your API. The requirement is to implement an authentication strategy which is similar to OAuth or SAML. Which of the following is the MOST suitable method that the developer should use in this scenario?
    - Cross-Account Lambda Authorizer
    - AWS STS-based authentication
    - Requesting Parameter-based Lambda Authorization
    - Token-based authorization

https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html

https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-lambda-authorizer-input.html

https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-lambda-authorizer-cross-account-lambda-authorizer.html

https://tutorialsdojo.com/amazon-api-gateway/

## Review Refactoring

## Review Deployment
- A company is heavily using a range of AWS services to host their enterprise applications. Currently, their deployment process still has a lot of manual steps which is why they plan to automate their software delivery process using continuous integration and delivery (CI/CD) pipelines in AWS. They will use CodePipeline to orchestrate each step of their release process and CodeDeploy for deploying applications to various compute platforms in AWS. In this architecture, which of the following are valid considerations when using CodeDeploy? (Select TWO.)
    - AWS Lambda compute platform deployments cannot use an in-place deployment type.
    - CodeDeploy can deploy applications to both your EC2 instances as well as your on-premises servers.
    - CodeDeploy can deploy applications to EC2, AWS Lambda, and Amazon ECS only
    - The CodeDeploy agent communicates using HTTP over port 80
    - You have to install and use the CodeDeploy agent installed on your EC2 instances and ECS cluster

https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html

https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent.html

https://aws.amazon.com/getting-started/projects/set-up-ci-cd-pipeline/

https://tutorialsdojo.com/aws-codedeploy/

https://www.youtube.com/watch?v=ClWBJT6k20Q

<p align="center">____________________</p>

- To accommodate a new application deployment, you have created a new EBS volume to be attached to your EC2 instance. After attaching the newly created EBS volume to the Linux EC2 instance, which of the following steps are you going to do next in order to use this volume?
    - Assign a file system on the volume using the AWS Console
    - Create a file system on this volume
    - Mount the volume since it already has a pre-configured file system
    - No action needed. AWS automatically configures the EBS volume for use on your instance

http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html

https://tutorialsdojo.com/amazon-elastic-compute-cloud-amazon-ec2/

https://tutorialsdojo.com/amazon-ebs/

<p align="center">____________________</p>

- Due to the popularity of serverless computing, your manager instructed you to share your technical expertise to the whole software development department of your company. You are planning to deploy a simple Node.js 'Hello World' Lambda function to AWS using CloudFormation. Which of the following is the EASIEST way of deploying the function to AWS?
    - Uploading the code in S3 as a ZIP file then specifying the S3 path in the ZipFile parameter of the AWS::Lambda::Function resource in the CloudFormation template
    - Including your function source inline in the Code parameter of the AWS::Lambda::Function resource in the CloudFormation template
    - Including your function source inline in the ZipFile parameter of the AWS::Lambda::Function resource in the CloudFormation template 
    - Uploading the code in S3 then specifying the S3Key and S3Bucket parameters under the AWS::Lambda::Function resource in the CloudFormation template

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html

https://tutorialsdojo.com/aws-cloudformation/

<p align="center">____________________</p>

- An application is hosted in Elastic Beanstalk which is currently running in Java 7 runtime environment. A new version of the application is ready to be deployed and the developer was tasked to upgrade the platform to Java 8 to accommodate the changes. Which of the following is the MOST appropriate action that the developer should do to upgrade the platform?
    - Update your Environment's Platform Version
    - Perform a Blue/Green Deployment 
    - Updating the environment's platform version to Java 8
    - Manually upgrading the Java runtime environment of the EC2 instances in the Elastic Beanstalk environment 
    - Performing a Canary deployment 

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.platform.upgrade.html#using-features.platform.upgrade.bluegreen

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.CNAMESwap.html

https://www.youtube.com/watch?v=rx7e7Fej1Oo

https://tutorialsdojo.com/aws-elastic-beanstalk/

https://tutorialsdojo.com/aws-certified-developer-associate/

<p align="center">____________________</p>

## Review Monitor and Troubleshooting
- A company has 5 different applications running on several On-Demand EC2 instances. The DevOps team is required to set up a graphical representation of the key performance metrics for each application. These system metrics must be available on a single shared screen for more effective and visible monitoring. Which of the following should the DevOps team do to satisfy this requirement using Amazon CloudWatch?
    - Set up a custom CloudWatch Alarm with a unique metric name for each application
    - Set up a custom CloudWatch namespace with a unique metric name for each application.
    - Set up a custom CloudWatch dimension with a unique metric name for each application
    - Set up a custom CloudWatch Event with a unique metric name for each application

https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Namespace

https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.html

https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html

https://tutorialsdojo.com/amazon-cloudwatch/

https://www.youtube.com/watch?v=q0DmxfyGkeU

<p align="center">____________________</p>

- A developer has instrumented an application using the X-Ray SDK to collect all data about the requests that an application serves. There is a new requirement to develop a custom debug tool which will enable them to view the full traces of their application without using the X-Ray console. What should the developer do to accomplish this task?
    - Use the GetGroup API to get the list of trace IDs of the application and then retrieving the list of traces using BatchGetTraces API
    - Use the GetTraceSummaries API to get the list of trace IDs of the application and then retrieve the list of traces using BatchGetTraces API
    - Use the GetServiceGraph API to get the list of trace IDs of the application and then retrieving the list of traces using GetTraceSummaries API 
    - Use the BatchGetTraces API to get the list of trace IDs of the application and then retrieving the list of traces using GetTraceSummaries API

https://docs.aws.amazon.com/xray/latest/devguide/xray-api-segmentdocuments.html

https://docs.aws.amazon.com/xray/latest/api/API_BatchGetTraces.html

https://tutorialsdojo.com/aws-x-ray/

<p align="center">____________________</p>

- A Docker application hosted on an ECS cluster has been encountering intermittent unavailability issues and time outs. The lead DevOps engineer instructed you to instrument the application to detect where high latencies are occurring and to determine the specific services and paths impacting application performance. Which of the following steps should you do to properly accomplish this task? (Select TWO.)
    - Configure the port mappings and network mode settings in your task definition file to allow traffic on UDP port 2000
    - Adding the xray-daemon.config configuration file in your Docker image
    - Create a Docker image that runs the X-Ray daemon, upload it to a Docker image repository, and then deploy it to your Amazon ECS cluster.
    - Manually installing the X-Ray daemon to the instances via a user data script
    - Configuring the port mappings and network mode settings in the container agent to allow traffic on TCP port 2000 

https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon-ecs.html

https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon.html

https://docs.aws.amazon.com/xray/latest/devguide/scorekeep-ecs.html

https://tutorialsdojo.com/aws-x-ray/

https://tutorialsdojo.com/instrumenting-your-application-with-aws-x-ray/

<p align="center">____________________</p>

- A developer is instrumenting an application which will be hosted in a large On-Demand EC2 instance in AWS. Which of the following are valid considerations in X-Ray that the developer should follow? (Select TWO.)
    - Set the namespace subsegment field to aws for AWS SDK calls and remote for other downstream calls
    - Setting the annotations object with any additional custom data that you want to store in the segment 
    - Set the metadata object with any additional custom data that you want to store in the segment.
    - Setting the namespace subsegment field to remote for AWS SDK calls and aws for other downstream calls
    - Setting the metadata object with key-value pairs that you want X-Ray to index for search

https://docs.aws.amazon.com/xray/latest/devguide/xray-api-segmentdocuments.html

https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html 

https://tutorialsdojo.com/aws-x-ray/

https://tutorialsdojo.com/instrumenting-your-application-with-aws-x-ray/

## Review Development with AWS services
- In order to quickly troubleshoot their systems, your manager instructed you to record the calls that your application makes to all AWS services and resources. You developed a custom code that will send the segment documents directly to X-Ray by using the PutTraceSegments API. What should you include in your segment document to meet the above requirement?
    - Annotations
    - Metadata
    - Subsegments
    - tracing header

https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html

https://docs.aws.amazon.com/xray/latest/devguide/xray-api-segmentdocuments.html#api-segmentdocuments-subsegments

https://tutorialsdojo.com/aws-x-ray/

https://tutorialsdojo.com/instrumenting-your-application-with-aws-x-ray/ 

<p align="center">____________________</p>

- A company has an AWS account with only 2 Lambda functions, which process data and store the results in an S3 bucket. An Application Load Balancer is used to distribute the incoming traffic to the two Lambda functions as registered targets. You noticed that in peak times, the first Lambda function works with optimal performance but the second one is throttling the incoming requests. Which of the following is the MOST likely root cause of this issue?
    - The concurrency execution limit provided to the first function is less than the second function 
    - The concurrency execution limit provided to the first function is significantly higher than the second function.
    - The concurrency execution limit provided to the first function is significantly higher than the second function.
    - The first function is using the unreserved account concurrency while the second function has been set with a concurrency execution limit of 1000

https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html

https://docs.aws.amazon.com/lambda/latest/dg/scaling.html

https://tutorialsdojo.com/aws-lambda/

<p align="center">____________________</p>

- A developer wants to use multi-factor authentication (MFA) to protect programmatic calls to specific AWS API operations like Amazon EC2 StopInstances. He needs to call an API where he can submit the MFA code that is associated with his MFA device. Using the temporary security credentials that are returned from the call, he can then make programmatic calls to API operations that require MFA authentication. Which API should the developer use to properly implement this security feature?
    - AssumeRoleWithWebIdentity 
    - AssumeRoleWithSAML
    - GetSessionToken
    - GetFederationToken

https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#stsapi_comparison

https://docs.aws.amazon.com/STS/latest/APIReference/API_GetSessionToken.html

https://tutorialsdojo.com/aws-identity-and-access-management-iam/

<p align="center">____________________</p>

- You recently deployed an application to a newly created AWS account, which uses two identical Lambda functions to process ad-hoc requests. The first function processes incoming requests efficiently but the second one has a longer processing time even though both of the functions have exactly the same code. Based on your monitoring, the Throttles metric of the second function is greater than the first one in Amazon CloudWatch. Which of the following are possible solutions that you can implement to fix this issue? (Select TWO.)
    - Set the concurrency execution limit of both functions to 450
    - Decrease the concurrency execution limit of the first function.
    - Setting the concurrency execution limit of both functions to 500
    - Configuring the second function to use an unreserved account concurrency
    - Setting the concurrency execution limit of the second function to 0 
 
https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html

https://docs.aws.amazon.com/lambda/latest/dg/scaling.html

https://tutorialsdojo.com/aws-lambda/

<p align="center">____________________</p>

- A developer is instructed to collect data on the number of times that web visitors click the advertisement link of a popular news website. A database entry containing the count will be incremented for every click. Given that the website has millions of readers worldwide, your database should be configured to provide optimal performance to capture all the click events. What is the BEST service that the developer should implement in this scenario?
    - Taking advantage of Amazon Aurora's performance speed and AUTO_INCREMENT feature for item updates
    - Launching an Amazon Redshift for the database and applying a step count of 1 for the IDENTITY column
    - Setup Amazon DynamoDB for the database and implement atomic counters for the UpdateItem operation of the website counter.
    - Using Amazon RDS for the database and setting up SQL AUTO_INCREMENT on your tables

https://aws.amazon.com/dynamodb/

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/WorkingWithItems.html#WorkingWithItems.AtomicCounters

https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_TABLE_NEW.html

https://tutorialsdojo.com/amazon-dynamodb/

<p align="center">____________________</p>

- An application in your development account is running in an AWS Elastic Beanstalk environment which has an attached Amazon RDS database. You noticed that if you terminate the environment, it also brings down the database which hinders you from performing seamless updates with blue-green deployments. This also poses a critical security risk if the company decides to deploy the application in production. In this scenario, how can you decouple your database instance from your environment without having any data loss?
    - Use the blue/green deployment strategy to decouple the Amazon RDS instance from your Elastic Beanstalk environment. Create an RDS DB snapshot of the database and enable deletion protection. Create a new Elastic Beanstalk environment with the necessary information to connect to the Amazon RDS instance. Before terminating the old Elastic Beanstalk environment, remove its security group rule first before proceeding
    - Use the blue/green deployment strategy to decouple the Amazon RDS instance from your Elastic Beanstalk environment. Create an RDS DB snapshot of the database and enable deletion protection. Create a new Elastic Beanstalk environment with the necessary information to connect to the Amazon RDS instance and delete the old environment
    - Use a Canary deployment strategy to decouple the Amazon RDS instance from your Elastic Beanstalk environment. Create an RDS DB snapshot of the database and enable deletion protection. Create a new Elastic Beanstalk environment with the necessary information to connect to the Amazon RDS instance and delete the old environment 
    - Use a Canary deployment strategy to decouple the Amazon RDS instance from your Elastic Beanstalk environment. Create an RDS DB snapshot of the database and then create a new Elastic Beanstalk environment with the necessary information to connect to the Amazon RDS instance

https://aws.amazon.com/premiumsupport/knowledge-center/decouple-rds-from-beanstalk/

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.RDS.html

https://tutorialsdojo.com/aws-elastic-beanstalk/

<p align="center">____________________</p>

- A company has a global multi-player game with a multi-master DynamoDB database topology which stores data in multiple AWS regions. You were assigned to develop a real-time data analytics application which will track and store the recent changes on all the tables from various regions. Only the new data of the recently updated item is needed to be tracked by your application. Which of the following is the MOST suitable way to configure the data analytics application to detect and retrieve the updated database entries automatically?
    - Enable DynamoDB Streams and set the value of StreamViewType to NEW_IMAGE. Create a trigger in AWS Lambda to capture stream data and forward it to your application
    - Enable DynamoDB Streams and set the value of StreamViewType to NEW_IMAGE then use Kinesis Adapter in the application to consume streams from DynamoDB
    - Enable DynamoDB Streams and set the value of StreamViewType to NEW_AND_OLD_IMAGE. Use Kinesis Adapter in the application to consume streams from DynamoDB 
    - Enable DynamoDB Streams and set the value of StreamViewType to NEW_AND_OLD_IMAGE. Create a trigger in AWS Lambda to capture stream data and forward it to your application

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.KCLAdapter.html

https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_StreamSpecification.html

https://tutorialsdojo.com/amazon-dynamodb/

https://tutorialsdojo.com/aws-lambda-integration-with-amazon-dynamodb-streams/

<p align="center">____________________</p>

- A developer needs to configure the environment name, solution stack, and environment links of his application environment which will be hosted in Elastic Beanstalk. Which configuration file should the developer add in the source bundle to meet the above requirement?
    - Dockerrun.aws.json
    - env.config
    - cron.yaml
    - env.yaml

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-cfg-manifest.html

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/applications-sourcebundle.html

https://tutorialsdojo.com/aws-elastic-beanstalk/

<p align="center">____________________</p>

- A write-heavy data analytics application is using DynamoDB database which has global secondary index. Whenever the application is performing heavy write activities on the table, the DynamoDB requests return a ProvisionedThroughputExceededException. Which of the following is the MOST likely cause of this issue?
    - The provisioned write capacity for the global secondary index is greater than the write capacity of the base table
    - The provisioned write capacity for the global secondary index is less than the write capacity of the base table.
    - The provisioned throughput exceeds the current throughput limit for your account
    - The rate of requests exceeds the allowed throughput

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.html#GSI.ThroughputConsiderations

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.Errors.html#Programming.Errors.MessagesAndCodes

https://tutorialsdojo.com/amazon-dynamodb/

https://tutorialsdojo.com/aws-certified-developer-associate/

<p align="center">____________________</p>

- A company has a central data repository in Amazon S3 that needs to be accessed by developers belonging to different AWS accounts. The required IAM role has been created with the appropriate S3 permissions. Given that the developers mostly interact with S3 via APIs, which API should the developers call to use the IAM role?
    - AssumeRoleWithWebIdentity
    - AssumeRole
    - AssumeRoleWithSAML
    - GetSessionToken 

https://aws.amazon.com/blogs/security/how-to-use-a-single-iam-user-to-easily-access-all-your-accounts-by-using-the-aws-cli/

https://aws.amazon.com/premiumsupport/knowledge-center/s3-instance-access-bucket/

https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html

https://tutorialsdojo.com/aws-identity-and-access-management-iam/

<p align="center">____________________</p>

- A data analytics company has installed sensors to track the number of people that goes to the mall. The data sets are collected in real-time by an Amazon Kinesis Data Stream which has a consumer that is configured to process data every other day and store the results to S3. Your team noticed that your S3 bucket is only receiving half of the data that is being sent to the Kinesis stream but after checking, you have verified that the sensors are properly sending the data to Amazon Kinesis in real-time without any issues. Which of the following is the MOST likely root cause of this issue?
    - By default, the data records are only accessible for 24 hours from the time they are added to a Kinesis stream.
    - The sensors are having intermittent connection issues
    - The Amazon Kinesis Data Stream has too many open shards
    - tTe Amazon Kinesis Data Stream automatically deletes duplicate data

http://docs.aws.amazon.com/streams/latest/dev/kinesis-extended-retention.html

https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-resharding.html

https://tutorialsdojo.com/amazon-kinesis/

<p align="center">____________________</p>

- Your team is developing a new feature on your application which is already hosted in Elastic Beanstalk. After several weeks, the new version of the application is ready to be deployed and you were instructed to handle the deployment. What is the correct way to deploy the new version to Elastic Beanstalk via the CLI?
    - Packaging your application as a zip file and deploying it using the eb deploy command
    - Packaging your application as a tar file and deploying it using the eb deploy command
    - Packaging your application as a zip file and deploying it using the aws elasticbeanstalk update-application command
    - Packaging your application as a tar file and deploying it using the aws elasticbeanstalk update-application command

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3.html

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-configuration.html#eb-cli3-artifact

https://tutorialsdojo.com/aws-elastic-beanstalk/

https://tutorialsdojo.com/elastic-beanstalk-vs-cloudformation-vs-opsworks-vs-codedeploy/

https://tutorialsdojo.com/comparison-of-aws-services/