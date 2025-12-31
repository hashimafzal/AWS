# Practice Test 6

- Score 78%
![PT 6 Results](../media/pt-6-results.png)

# ToDo list review:
- Security
- Refactoring
- Deployment
    - Review ECS config file (/etc/ecs/ecs.config)
- Monitor and Troubleshooting
    - [ELB troubleshooting error codes](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-troubleshooting.html)
- Review Development with AWS services
    - [EFS Storage classes](https://docs.aws.amazon.com/efs/latest/ug/storage-classes.html)
    - Sharing EB environment configurations between accounts


## Review Security
- An analytics company is using Kinesis Data Streams (KDS) to process automobile health-status data from the taxis managed by a taxi ride-hailing service. Multiple consumer applications are using the incoming data streams and the engineers have noticed a performance lag for the data delivery speed between producers and consumers of the data streams. As a Developer Associate, which of the following options would you suggest for improving the performance for the given use-case?
    - Swap out Kinesis Data Streams with Kinesis Data Firehose 
    - Use Enhanced Fanout feature of Kinesis Data Streams
    - Swap out Kinesis Data Streams with SQS Standard queues
    - Swap out Kinesis Data Streams with SQS FIFO queues

https://aws.amazon.com/blogs/aws/kds-enhanced-fanout/

https://aws.amazon.com/kinesis/data-streams/faqs/


<p align="center">____________________</p>

- A Company uses a large set of EBS volumes for their fleet of Amazon EC2 instances. As an AWS Certified Developer Associate, your help has been requested to understand the security features of the EBS volumes. The company does not want to build or maintain their own encryption key management infrastructure. Can you help them understand what works for Amazon EBS encryption? (Select two)
    - Encryption by default is a Region-specific setting. If you enable it for a Region, you cannot disable it for individual volumes or snapshots in that Region
    - You can encrypt an existing unencrypted volume or snapshot by using AWS Key Management Service (KMS) AWS SDKs 
    - A volume restored from an encrypted snapshot, or a copy of an encrypted snapshot, is always encrypted
    - A snapshot of an encrypted volume can be encrypted or unencrypted
    - Encryption by default is an AZ specific setting. If you enable it for an AZ, you cannot disable it for individual volumes or snapshots in that AZ

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encrypt-unencrypted


<p align="center">____________________</p>

- A photo-sharing application manages its EC2 server fleet running behind an Application Load Balancer and the traffic is fronted by a CloudFront distribution. The development team wants to decouple the user authentication process for the application so that the application servers can just focus on the business logic. As a Developer Associate, which of the following solutions would you recommend to address this use-case with minimal development effort?
    - Use Cognito Authentication via Cognito Identity Pools for your Application Load Balancer
    - Use Cognito Authentication via Cognito User Pools for your Application Load Balancer
    - Use Cognito Authentication via Cognito User Pools for your CloudFront distribution
    - Use Cognito Authentication via Cognito Identity Pools for your CloudFront distribution

https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-authenticate-users.html

https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html

https://aws.amazon.com/blogs/networking-and-content-delivery/authorizationedge-using-cookies-protect-your-amazon-cloudfront-content-from-being-downloaded-by-unauthenticated-users/



## Review Refactoring
- A video streaming application uses Amazon CloudFront for its data distribution. The development team has decided to use CloudFront with origin failover for high availability. Which of the following options are correct while configuring CloudFront with Origin Groups? (Select two)
    - CloudFront fails over to the secondary origin only when the HTTP method of the viewer request is GET, HEAD or OPTIONS
    - When there’s a cache hit, CloudFront routes the request to the primary origin in the origin group 
    - To set up origin failover, you must have a distribution with at least three origins
    - In the Origin Group of your distribution, all the origins are defined as primary for automatic failover in case an origin fails
    - CloudFront routes all incoming requests to the primary origin, even when a previous request failed over to the secondary origin

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/high_availability_origin_failover.html

<p align="center">____________________</p>

- A development team has noticed that one of the EC2 instances has been wrongly configured with the 'DeleteOnTermination' attribute set to True for its root EBS volume. As a developer associate, can you suggest a way to disable this flag while the instance is still running?
    - Set the DeleteOnTermination attribute to False using the command line
    - Update the attribute using AWS management console. Select the EC2 instance and then uncheck the Delete On Termination check box for the root EBS volume
    - Set the DisableApiTermination attribute of the instance using the API 
    - The attribute cannot be updated when the instance is running. Stop the instance from Amazon EC2 console and then update the flag 

https://aws.amazon.com/premiumsupport/knowledge-center/deleteontermination-ebs/

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#delete-on-termination-running-instance

<p align="center">____________________</p>

- A developer is configuring the redirect actions for an Application Load Balancer. The developer stumbled upon the following snippet of code. Which of the following is an example of a query string condition that the developer can use on AWS CLI?
    - 
    ```json
    [
    {
        "Field": "query-string",
        "PathPatternConfig": {
            "Values": ["/img/*"]
        }
    }
    ]
    ```
        - 
    ```json
    [
    {
        "Type": "redirect",
        "RedirectConfig": {
            "Protocol": "HTTPS",
            "Port": "443",
            "Host": "#{host}",
            "Path": "/#{path}",
            "Query": "#{query}",
            "StatusCode": "HTTP_301"
        }
    }
    ]
    ```
        - 
    ```json
    [
    {
        "Field": "query-string",
        "StringHeaderConfig": {
            "Values": ["*.example.com"]
        }
    }
    ]
    ```
        - 
    ```json
    [
    {
        "Field": "query-string",
        "QueryStringConfig": {
            "Values": [
                {
                    "Key": "version",
                    "Value": "v1"
                },
                {
                    "Value": "*example*"
                }
            ]
        }
    }
    ]
    ```

https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html#query-string-conditions

<p align="center">____________________</p>

- An organization with high data volume workloads have successfully moved to DynamoDB after having many issues with traditional database systems. However, a few months into production, DynamoDB tables are consistently recording high latency. As a Developer Associate, which of the following would you suggest to reduce the latency? (Select two)
    - Use eventually consistent reads in place of strongly consistent reads whenever possible
    - Increase the request timeout settings, so the client gets enough time to complete the requests, thereby reducing retries on the system
    - Reduce connection pooling, which keeps the connections alive even when user requests are not present, thereby, blocking the services 
    - Use DynamoDB Accelerator (DAX) for businesses with heavy write-only workloads 
    - Consider using Global tables if your application is accessed by globally distributed users

https://aws.amazon.com/premiumsupport/knowledge-center/dynamodb-high-latency/

https://aws.amazon.com/dynamodb/

<p align="center">____________________</p>

- A development team has been using Amazon S3 service as an object store. With Amazon S3 turning strongly consistent, the team wants to understand the impact of this change on its data storage practices. As a developer associate, can you identify the key characteristics of the strongly consistent data model followed by S3? (Select two)
    - A process replaces an existing object and immediately tries to read it. Amazon S3 might return the old data
    - A process deletes an existing object and immediately tries to read it. Amazon S3 can return data as the object deletion has not yet propagated completely 
    - A process deletes an existing object and immediately tries to read it. Amazon S3 will not return any data as the object has been deleted 
    - A process deletes an existing object and immediately lists keys within its bucket. The object could still be visible for few more minutes till the change propagates
    - If you delete a bucket and immediately list all buckets, the deleted bucket might still appear in the list 

https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html#ConsistencyModel


## Review Deployment
- You are working for a technology startup building web and mobile applications. You would like to pull Docker images from the ECR repository called demo so you can start running local tests against the latest application version. Which of the following commands must you run to pull existing Docker images from ECR? (Select two)
    - aws docker push 1234567890.dkr.ecr.eu-west-1.amazonaws.com/demo:latest
    - docker pull 1234567890.dkr.ecr.eu-west-1.amazonaws.com/demo:latest
    - docker login -u $AWS_ACCESS_KEY_ID -p $AWS_SECRET_ACCESS_KEY
    - $(aws ecr get-login --no-include-email)
    - docker build -t 1234567890.dkr.ecr.eu-west-1.amazonaws.com/demo:latest 

https://docs.aws.amazon.com/cli/latest/reference/ecr/get-login.html

<p align="center">____________________</p>

- A developer is creating a RESTful API service using an Amazon API Gateway with AWS Lambda integration. The service must support different API versions for testing purposes. As a Developer Associate, which of the following would you suggest as the best way to accomplish this?
    - Deploy the API versions as unique stages with unique endpoints and use stage variables to provide the context to identify the API versions
    - Use an X-Version header to identify which version is being called and pass that header to the Lambda function
    - Use an API Gateway Lambda authorizer to route API clients to the correct API version
    - Set up an API Gateway resource policy to identify the API versions and provide context to the Lambda function 

https://docs.aws.amazon.com/apigateway/latest/developerguide/stage-variables.html

https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-resource-policies.html

https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html

## Review Monitor and Troubleshooting

- A multi-national company runs its technology operations on AWS Cloud. As part of their storage solution, they use a large number of EBS volumes, with AWS Config and CloudTrail activated. A manager has tried to find the user name that created an EBS volume by searching CloudTrail events logs but wasn't successful. As a Developer Associate, which of the following would you recommend as the correct solution?
    - AWS CloudTrail event logs for 'CreateVolume' aren't available for EBS volumes created during an Amazon EC2 launch
    - AWS CloudTrail event logs for 'ManageVolume' aren't available for EBS volumes created during an Amazon EC2 launch
    - Amazon EBS CloudWatch metrics are disabled 
    - EBS volume status checks are disabled

https://aws.amazon.com/premiumsupport/knowledge-center/find-ebs-user-config-cloudtrail/

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using_cloudwatch_ebs.html

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-volume-status.html

<p align="center">____________________</p>

- Your team-mate has configured an Amazon S3 event notification for an S3 bucket that holds sensitive audit data of a firm. As the Team Lead, you are receiving the SNS notifications for every event in this bucket. After validating the event data, you realized that few events are missing. What could be the reason for this behavior and how to avoid this in the future?
    - Your notification action is writing to the same bucket that triggers the notification
    - Versioning is enabled on the S3 bucket and event notifications are getting fired for only one version
    - If two writes are made to a single non-versioned object at the same time, it is possible that only a single event notification will be sent 
    - Someone could have created a new notification configuration and that has overridden your existing configuration

<p align="center">____________________</p>

- A startup manages its Cloud resources with Elastic Beanstalk. The environment consists of few Amazon EC2 instances, an Auto Scaling Group (ASG), and an Elastic Load Balancer. Even after the Load Balancer marked an EC2 instance as unhealthy, the ASG has not replaced it with a healthy instance. As a Developer, suggest the necessary configurations to automate the replacement of unhealthy instance.
    - Auto Scaling group doesn't automatically replace the unhealthy instances marked by the load balancer. They have to be manually replaced from AWS Console
    - The health check type of your instance's Auto Scaling group, must be changed from EC2 to ELB by using a configuration file 
    - The ping path field of the Load Balancer is configured incorrectly 
    - Health check parameters were configured for checking the instance health alone. The instance failed because of application failure which was not configured as a parameter for health check status 

https://aws.amazon.com/premiumsupport/knowledge-center/elastic-beanstalk-instance-automation/

https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-healthchecks.html

<p align="center">____________________</p>

- A company uses microservices-based infrastructure to process the API calls from clients, perform request filtering and cache requests using the AWS API Gateway. Users report receiving 501 error code and you have been contacted to find out what is failing. Which service will you choose to help you troubleshoot?
    - Use X-Ray service
    - Use CloudTrail service 
    - Use API Gateway service 
    - Use CloudWatch service 

https://aws.amazon.com/cloudtrail/

https://aws.amazon.com/api-gateway/

https://aws.amazon.com/cloudwatch/features/

## Review Development with AWS services
- A developer at a university is encrypting a large XML payload transferred over the network using AWS KMS and wants to test the application before going to production. What is the maximum data size supported by AWS KMS?
    - 10 MB
    - 1 MB
    - 16 KB
    - 4 KB

<p align="center">____________________</p>

- A company is looking at storing their less frequently accessed files on AWS that can be concurrently accessed by hundreds of EC2 instances. The company needs the most cost-effective file storage service that provides immediate access to data whenever needed. Which of the following options represents the best solution for the given requirements?
    - Amazon S3 Standard-Infrequent Access (S3 Standard-IA) storage class
    - Amazon Elastic File System (EFS) Standard–IA storage class 
    - Amazon Elastic Block Store (EBS)
    - Amazon Elastic File System (EFS) Standard storage class

https://docs.aws.amazon.com/efs/latest/ug/storage-classes.html

<p align="center">____________________</p>

- The development team at a health-care company is planning to migrate to AWS Cloud from the on-premises data center. The team is evaluating Amazon RDS as the database tier for its flagship application. Which of the following would you identify as correct for RDS Multi-AZ? (Select two)
    - Updates to your DB Instance are asynchronously replicated across the Availability Zone to the standby in order to keep both in sync
    - For automated backups, I/O activity is suspended on your primary DB since backups are not taken from standby
    - RDS applies OS updates by performing maintenance on the standby, then promoting the standby to primary, and finally performing maintenance on the old primary, which becomes the new standby
    - To enhance read scalability, a Multi-AZ standby instance can be used to serve read requests
    - Amazon RDS automatically initiates a failover to the standby, in case the primary database fails for any reason

https://aws.amazon.com/rds/faqs/

<p align="center">____________________</p>

- A multi-national company maintains separate AWS accounts for different verticals in their organization. The project manager of a team wants to migrate the Elastic Beanstalk environment from Team A's AWS account into Team B's AWS account. As a Developer, you have been roped in to help him in this process. Which of the following will you suggest?
    - Create an export configuration from the Elastic Beanstalk console from Team A's account. This configuration has to be shared with the IAM Role of Team B's account. The import option of the Team B's account will show the saved configuration, that can be used to create a new Beanstalk application
    - Create a saved configuration in Team A's account and configure it to Export. Now, log into Team B's account and choose the Import option. Here, you need to specify the name of the saved configuration and allow the system to create the new application. This takes a little time based on the Regions the two accounts belong to 
    - It is not possible to migrate Elastic Beanstalk environment from one AWS account to the other
    - Create a saved configuration in Team A's account and download it to your local machine. Make the account-specific parameter changes and upload to the S3 bucket in Team B's account. From Elastic Beanstalk console, create an application from 'Saved Configurations

https://aws.amazon.com/premiumsupport/knowledge-center/elastic-beanstalk-migration-accounts/

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-configuration-savedconfig.html

<p align="center">____________________</p>

- Your company has a load balancer in a VPC configured to be internet facing. The public DNS name assigned to the load balancer is myDns-1234567890.us-east-1.elb.amazonaws.com. When your client applications first load they capture the load balancer DNS name and then resolve the IP address for the load balancer so that they can directly reference the underlying IP. It is observed that the client applications work well but unexpectedly stop working after a while. What is the reason for this?
    - You need to disable multi-AZ deployments
    - Your security groups are not stable
    - The load balancer is highly available and its public IP may change. The DNS name is constant
    - You need to enable stickiness

https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-internet-facing-load-balancers.html

<p align="center">____________________</p>

- As a Developer, you are working on a mobile application that utilizes Amazon Simple Queue Service (SQS) for sending messages to downstream systems for further processing. One of the requirements is that the messages should be stored in the queue for a period of 12 days. How will you configure this requirement?
    - Enable Long Polling for the SQS queue
    - The maximum retention period of SQS messages is 7 days, therefore retention period of 12 days is not possible 
    - Use a FIFO SQS queue
    - Change the queue message retention setting 

https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-basic-architecture.html

https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html

https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html

<p align="center">____________________</p>

- An investment firm wants to continuously generate time-series analytics of the stocks being purchased by its customers. The firm wants to build a live leaderboard with real-time analytics for these in-demand stocks. Which of the following represents a fully managed solution to address this use-case?
    - Use Kinesis Firehose to ingest data and Kinesis Data Analytics to generate leaderboard scores and time-series analytics
    - Use Kinesis Data Streams to ingest data and Kinesis Data Analytics to generate leaderboard scores and time-series analytics
    - Use Kinesis Data Streams to ingest data and Amazon Kinesis Client Library to the application logic to generate leaderboard scores and time-series analytics
    - Use Kinesis Firehose to ingest data and Amazon Athena to generate leaderboard scores and time-series analytics

https://docs.aws.amazon.com/firehose/latest/dev/data-analysis.html

https://aws.amazon.com/kinesis/data-analytics/faqs/

<p align="center">____________________</p>

- The development team at a retail organization wants to allow a Lambda function in its AWS Account A to access a DynamoDB table in another AWS Account B. As a Developer Associate, which of the following solutions would you recommend for the given use-case?
    - Create a clone of the Lambda function in AWS Account B so that it can access the DynamoDB table in the same account
    - Create an IAM role in Account B with access to DynamoDB. Modify the trust policy of the execution role in Account A to allow the execution role of Lambda to assume the IAM role in Account B. Update the Lambda function code to add the AssumeRole API call 
    - Create an IAM role in account B with access to DynamoDB. Modify the trust policy of the role in Account B to allow the execution role of Lambda to assume this role. Update the Lambda function code to add the AssumeRole API call
    - Add a resource policy to the DynamoDB table in AWS Account B to give access to the Lambda function in Account A

 https://aws.amazon.com/premiumsupport/knowledge-center/lambda-function-assume-iam-role/

 