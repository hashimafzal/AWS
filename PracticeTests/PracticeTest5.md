# Practice Test 5

- Score 86%
![PT 5 Results](../media/pt-5-results.png)

# ToDo list review:
- Security
    - VPC endpoints and how they connect to AWS services privately
    - STS support in API gateway (does it exist?)
- Refactoring
    - [S3 pagination](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-pagination.html)
- Deployment
    - [EB supported platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html#platforms-supported.mcdocker)
- Monitor and Troubleshooting
- Review Development with AWS services
- Others
    - Review CodeBuild Security (encrypted artifacts?)
    - EB version lifecycle policies
    - EB Cron.yaml
    - ELB error codes troubleshooting
    - LSI and GSI review


## Review Security
- An e-commerce company has multiple EC2 instances operating in a private subnet which is part of a custom VPC. These instances are running an image processing application that needs to access images stored on S3. Once each image is processed, the status of the corresponding record needs to be marked as completed in a DynamoDB table. How would you go about providing private access to these AWS resources which are not part of this custom VPC?
    - Create a gateway endpoint for S3 and add it as a target in the route table of the custom VPC. Create an interface endpoint for DynamoDB and then connect to the DynamoDB service using the private IP address
    - Create a separate gateway endpoint for S3 and DynamoDB each. Add two new target entries for these two gateway endpoints in the route table of the custom VPC
    - Create a separate interface endpoint for S3 and DynamoDB each. Then connect to these services using the private IP address
    - Create a gateway endpoint for DynamoDB and add it as a target in the route table of the custom VPC. Create an API endpoint for S3 and then connect to the S3 service using the private IP address 

https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html

https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html

<p align="center">____________________</p>

- You've just deployed an AWS Lambda function. The lambda function will be invoked via the API Gateway. The API Gateway will need to control access to it. Which of the following mechanisms is not supported for API Gateway?
    - Lambda Authorizer
    - IAM permissions with sigv4
    - Cognito User Pools
    - STS

https://aws.amazon.com/api-gateway/

<p align="center">____________________</p>

- Your company likes to operate multiple AWS accounts so that teams have their environments. Services deployed across these accounts interact with one another, and now there's a requirement to implement X-Ray traces across all your applications deployed on EC2 instances and AWS accounts. As such, you would like to have a unified account to view all the traces. What should you in your X-Ray daemon set up to make this work? (Select two)
    - Configure the X-Ray daemon to use access and secret keys
    - Configure the X-Ray daemon to use an IAM instance role
    - Create a user in the target unified account and generate access and secret keys
    - Create a role in the target unified account and allow roles in each sub-account to assume the role
    - Enable Cross Account collection in the X-Ray console

https://aws.amazon.com/xray/faqs/

https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon-configuration.html

## Review Refactoring
- A data analytics company ingests a large number of messages and stores them in an RDS database using Lambda. Because of the increased payload size, it is taking more than 15 minutes to process each message. As a Developer Associate, which of the following options would you recommend to process each message in the MOST scalable way?
    - Contact AWS Support to increase the Lambda timeout to 60 minutes
    - Use DynamoDB instead of RDS as database
    - Provision EC2 instances in an Auto Scaling group to poll the messages from an SQS queue
    - Provision an EC2 instance to poll the messages from an SQS queue -

https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html

<p align="center">____________________</p>

- You are using AWS SQS FIFO queues to get the ordering of messages on a per user_id basis. On top of this, you would like to make sure that duplicate messages should not be sent to SQS as this would cause application failure. As a developer, which message parameter should you set for deduplicating messages?
    - MessageDeduplicationId
    - ReceiveRequestAttemptId
    - MessageGroupId
    - ContentBasedDeduplication

https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-messagededuplicationid-property.html

<p align="center">____________________</p>

- A company has recently launched a new gaming application that the users are adopting rapidly. The company uses RDS MySQL as the database. The development team wants an urgent solution to this issue where the rapidly increasing workload might exceed the available database storage. As a developer associate, which of the following solutions would you recommend so that it requires minimum development effort to address this requirement?
    - Create read replica for RDS MySQL 
    - Migrate RDS MySQL database to DynamoDB which automatically allocates storage space when required
    - Migrate RDS MySQL to Aurora which offers storage auto-scaling 
    - Enable storage auto-scaling for RDS MySQL

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html

<p align="center">____________________</p>

- You are running a public DNS service on an EC2 instance where the DNS name is pointing to the IP address of the instance. You wish to upgrade your DNS service but would like to do it without any downtime. Which of the following options will help you accomplish this?
    - Create a Load Balancer and an auto-scaling group 
    - Provide a static private IP 
    - Use Route 53 
    - Elastic IP

Route 53 is a DNS managed by AWS, but nothing prevents you from running your own DNS (it's just a software) on an EC2 instance. The trick of this question is that it's about EC2, running some software that needs a fixed IP, and not about Route 53 at all. DNS services are identified by a public IP, so you need to use Elastic IP.

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html#using-instance-addressing-eips-associating-different

<p align="center">____________________</p>

- You would like to paginate the results of an S3 List to show 100 results per page to your users and minimize the number of API calls that you will use. Which CLI options should you use? (Select two)
    - --limit
    - --starting-token
    - --next-token
    - --max-items
    - --page-size

## Review Deployment
- Your client wants to deploy a service on EC2 instances, and as EC2 instances are added into an ASG, each EC2 instance should be running 3 different Docker Containers simultaneously. What Elastic Beanstalk platform should they choose?
    - Docker multi-container platform
    - Custom platform
    - Third-party platform
    - Docker single-container platform

https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html#platforms-supported.mcdocker

<p align="center">____________________</p>

- You have created a test environment in Elastic Beanstalk and as part of that environment, you have created an RDS database. How can you make sure the database can be explored after the environment is destroyed?
    - Make a selective delete in EB
    - Make a snapshot of the database before it gets deleted
    - Change the Elastic Beanstalk environment variables 
    - Convert the Elastic Beanstalk environment to a worker environment

https://aws.amazon.com/premiumsupport/knowledge-center/decouple-rds-from-beanstalk/

## Review Monitor and Troubleshooting
- You are responsible for an application that runs on multiple Amazon EC2 instances. In front of the instances is an Internet-facing load balancer that takes requests from clients over the internet and distributes them to the EC2 instances. A health check is configured to ping the index.html page found in the root directory for the health status. When accessing the website via the internet visitors of the website receive timeout errors. What should be checked first to resolve the issue?
    - IAM Roles
    - Security Groups
    - The application is down
    - The ALB is warming up

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.html#TroubleshootingInstancesConnectionTimeout

<p align="center">____________________</p>

- Your client has tasked you with finding a service that would enable you to get cross-account tracing and visualization. Which service do you recommend?
    - X Ray
    - CloudWatch Events
    - VPC Flow Logs
    - CloudTrail

https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html

<p align="center">____________________</p>

- Which environment variable can be used by AWS X-Ray SDK to ensure that the daemon is correctly discovered on ECS?
    - AWS_XRAY_TRACING_NAME 
    - AWS_XRAY_DAEMON_ADDRESS
    - AWS_XRAY_CONTEXT_MISSING 
    - AWS_XRAY_DEBUG_MODE

https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-nodejs-configuration.html

<p align="center">____________________</p>

- A development team has a mix of applications hosted on-premises as well as on EC2 instances. The on-premises application controls all applications deployed on the EC2 instances. In case of any errors, the team wants to leverage Amazon CloudWatch to monitor and troubleshoot the on-premises application. As a Developer Associate, which of the following solutions would you suggest to address this use-case?
    - Upload log files from the on-premises server to an EC2 instance which further forwards the logs to CloudWatch
    - Upload log files from the on-premises server to S3 and let CloudWatch process the files from S3
    - Configure the CloudWatch agent on the on-premises server by using IAM user credentials with permissions for CloudWatch
    - Configure CloudWatch Logs to directly read the logs from the on-premises server

https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-premise.html

<p align="center">____________________</p>

- An IT company leverages CodePipeline to automate its release pipelines. The development team wants to write a Lambda function that will send notifications for state changes within the pipeline. As a Developer Associate, which steps would you suggest to associate the Lambda function with the event source?
    - Set up an Amazon CloudWatch Events rule that uses CodePipeline as an event source with the target as the Lambda function
    - Set up an Amazon CloudWatch alarm that monitors status changes in Code Pipeline and triggers the Lambda function
    - Use the Lambda console to configure a trigger that invokes the Lambda function with CodePipeline as the event source
    - Use the CodePipeline console to set up a trigger for the Lambda function 

https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html

https://docs.aws.amazon.com/codepipeline/latest/userguide/detect-state-changes-cloudwatch-events.html

## Review Development with AWS services
- A developer has created a new Application Load Balancer but has not registered any targets with the target groups. Which of the following errors would be generated by the Load Balancer?
    - HTTP 500: Internal server error
    - HTTP 503: Service unavailable
    - HTTP 502: Bad gateway
    - HTTP 504: Gateway timeout

https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-troubleshooting.html

<p align="center">____________________</p>

- A company ingests real-time data into its on-premises data center and subsequently a daily data feed is compressed into a single file and uploaded on Amazon S3 for backup. The typical compressed file size is around 2 GB. Which of the following is the fastest way to upload the daily compressed file into S3?
    - Upload the compressed file using multipart upload with S3 transfer acceleration
    - Upload the compressed file in a single operation 
    - Upload the compressed file using multipart upload 
    - FTP the compressed file into an EC2 instance that runs in the same region as the S3 bucket. Then transfer the file from the EC2 instance into the S3 bucket

https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html

https://docs.aws.amazon.com/AmazonS3/latest/dev/uploadobjusingmpu.html

<p align="center">____________________</p>

- You would like your Elastic Beanstalk environment to expose an HTTPS endpoint instead of an HTTP endpoint to get in-flight encryption between your clients and your web servers. What must be done to set up HTTPS on Beanstalk?
    - Create a config file in the .ebextensions folder to configure the Load Balancer
    - Use a separate CloudFormation template to load the SSL certificate onto the Load Balancer 
    - Configure Health Checks
    - Open up the port 80 for the security group 

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https-elb.html

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https.html

<p align="center">____________________</p>

- You have created a DynamoDB table to support your application and provisioned RCU and WCU to it so that your application has been running for over a year now without any throttling issues. Your application now requires a second type of query over your table and as such, you have decided to create an LSI and a GSI on a new table to support that use case. One month after having implemented such indexes, it seems your table is experiencing throttling. Upon looking at the table's metrics, it seems the RCU and WCU provisioned are still sufficient. What's happening?
    - Adding both an LSI and a GSI to a table is not recommended by AWS best practices as this is a known cause for creating throttles 
    - Metrics are lagging in your CloudWatch dashboard and you should see the RCU and WCU peaking for the main table in a few minutes
    - The GSI is throttling so you need to provision more RCU and WCU to the GSI
    - The LSI is throttling so you need to provision more RCU and WCU to the LSI

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.html#GSI.ThroughputConsiderations

<p align="center">____________________</p>

- One of your Kinesis Stream is experiencing increased traffic due to a sale day. Therefore your Kinesis Administrator has split shards and thus you went from having 6 shards to having 10 shards in your Kinesis Stream. Your consuming application is running a KCL-based application on EC2 instances. What is the maximum number of EC2 instances that can be deployed to process the shards?
    - 6
    - 20
    - 1
    - 10

https://docs.aws.amazon.com/streams/latest/dev/developing-consumers-with-kcl.html

