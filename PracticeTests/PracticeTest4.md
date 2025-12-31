# Practice Test 4
- Score 81%
![PT 4 Results](../media/pt-4-results.png)

# ToDo list review:
- Security
- Refactoring
- Deployment
- Monitor and Troubleshooting
- Review Development with AWS services
    - [ALB Target groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html)
    - VPC NACL (https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html, https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)
    - ~~[Routing in ELB](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html)~~


## Review Security
- A development team had enabled and configured CloudTrail for all the Amazon S3 buckets used in a project. The project manager owns all the S3 buckets used in the project. However, the manager noticed that he did not receive any object-level API access logs when the data was read by another AWS account. What could be the reason for this behavior/error?
    - The bucket owner also needs to be object owner to get the object access logs
    - The meta-data of the bucket is in an invalid state and needs to be corrected by the bucket owner from AWS console to fix the issue.
    - CloudTrail always delivers object-level API access logs to the requester and not to object owner
    - CloudTrail needs to be configured on both the AWS accounts for receiving the access logs in cross-account access

https://docs.aws.amazon.com/AmazonS3/latest/userguide/cloudtrail-logging-s3-info.html#cloudtrail-object-level-crossaccount

<p align="center">____________________</p>

- Your company stores confidential data on an Amazon Simple Storage Service (S3) bucket. New security compliance guidelines require that files be stored with server-side encryption. The encryption used must be Advanced Encryption Standard (AES-256) and the company does not want to manage S3 encryption keys. Which of the following options should you use?
    - SSE-S3
    - SSE-KMS
    - SSE-C
    - Client Side Encryption

https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingEncryption.html

<p align="center">____________________</p>

- Your company leverages Amazon CloudFront to provide content via the internet to customers with low latency. Aside from latency, security is another concern and you are looking for help in enforcing end-to-end connections using HTTPS so that content is protected. Which of the following options is available for HTTPS in AWS CloudFront?
    - Between clients and CloudFront as well as between CloudFront and backend
    - Between clients and CloudFront only
    - Neither between clients and CloudFront nor between CloudFront and backend
    - Between CloudFront and backend only

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html#secure-connections-supported-ciphers-cloudfront-to-origin

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.html

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-cloudfront-to-custom-origin.html

<p align="center">____________________</p>

- You have a popular web application that accesses data stored in an Amazon Simple Storage Service (S3) bucket. Developers use the SDK to maintain the application and add new features. Security compliance requests that all new objects uploaded to S3 be encrypted using SSE-S3 at the time of upload. Which of the following headers must the developers add to their request?
    - 'x-amz-server-side-encryption': 'AES256'
    - 'x-amz-server-side-encryption': 'SSE-S3'
    - 'x-amz-server-side-encryption': 'SSE-KMS'
    - 'x-amz-server-side-encryption': 'aws:kms'

https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html

https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingEncryption.html

<p align="center">____________________</p>

- An organization recently began using AWS CodeCommit for its source control service. A compliance security team visiting the organization was auditing the software development process and noticed developers making many git push commands within their development machines. The compliance team requires that encryption be used for this activity. How can the organization ensure source code is encrypted in transit and at rest?
    - Repositories are automatically encrypted at rest
    - Enable KMS encryption 
    - Use AWS Lambda as a hook to encrypt the pushed code
    - Use a git command line hook to encrypt the code client-side

https://docs.aws.amazon.com/codecommit/latest/userguide/encryption.html

<p align="center">____________________</p>

- As part of internal regulations, you must ensure that all communications to Amazon S3 are encrypted. For which of the following encryption mechanisms will a request get rejected if the connection is not using HTTPS?
    - SSE-KMS
    - SSE-S3
    - SSE-C
    - Client Side Encryption

https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerSideEncryptionCustomerKeys.html

<p align="center">____________________</p>

- An Amazon Simple Queue Service (SQS) has to be configured between two AWS accounts for shared access to the queue. AWS account A has the SQS queue in its account and AWS account B has to be given access to this queue. Which of the following options need to be combined to allow this cross-account access? (Select three)
    - The account A administrator creates an IAM role and attaches a permissions policy
    - The account B administrator creates an IAM role and attaches a trust policy to the role with account B as the principal 
    - The account A administrator attaches a trust policy to the role that identifies account B as the principal who can assume the role
    - The account A administrator delegates the permission to assume the role to any users in account A 
    - The account A administrator attaches a trust policy to the role that identifies account B as the AWS service principal who can assume the role 
    - The account B administrator delegates the permission to assume the role to any users in account B

https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-overview-of-managing-access.html

<p align="center">____________________</p>

- A company would like to migrate the existing application code from a GitHub repository to AWS CodeCommit. As an AWS Certified Developer Associate, which of the following would you recommend for migrating the cloned repository to CodeCommit over HTTPS?
    - Use IAM user secret access key and access key ID
    - Use IAM MFA
    - Use authentication offered by Github secure tokens
    - Use Git credentials generated from IAM

https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control.html

https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-gc.html

## Review Refactoring
- A company wants to add geospatial capabilities to the cache layer, along with query capabilities and an ability to horizontally scale. The company uses Amazon RDS as the database tier. Which solution is optimal for this use-case?
    - Use CloudFront caching to cater to demands of increasing workloads 
    - Migrate to Amazon DynamoDB to utilize the automatically integrated DynamoDB Accelerator (DAX) along with query capability features
    - Leverage the capabilities offered by ElastiCache for Redis with cluster mode enabled
    - Leverage the capabilities offered by ElastiCache for Redis with cluster mode disabled

https://aws.amazon.com/blogs/database/work-with-cluster-mode-on-amazon-elasticache-for-redis/

https://aws.amazon.com/blogs/database/amazon-elasticache-utilizing-redis-geospatial-capabilities/

<p align="center">____________________</p>

- A company has several Linux-based EC2 instances that generate various log files which need to be analyzed for security and compliance purposes. The company wants to use Kinesis Data Streams (KDS) to analyze this log data. Which of the following is the most optimal way of sending log data from the EC2 instances to KDS?
    - Use Kinesis Producer Library (KPL) to collect and ingest data from each EC2 instance
    - Install AWS SDK on each of the instances and configure it to send the necessary files to Kinesis Data Streams 
    - Run cron job on each of the instances to collect log data and send it to Kinesis Data Streams 
    - Install and configure Kinesis Agent on each of the instances

https://docs.aws.amazon.com/streams/latest/dev/writing-with-agents.html

## Review Deployment
- Your company is in the process of building a DevOps culture and is moving all of its on-premise resources to the cloud using serverless architectures and automated deployments. You have created a CloudFormation template in YAML that uses an AWS Lambda function to pull HTML files from GitHub and place them into an Amazon Simple Storage Service (S3) bucket that you specify. Which of the following AWS CLI commands can you use to upload AWS Lambda functions and AWS CloudFormation templates to AWS?
    - cloudformation package and cloudformation upload
    - cloudformation zip and cloudformation upload
    - cloudformation package and cloudformation deploy
    - cloudformation zip and cloudformation deploy

https://docs.aws.amazon.com/cli/latest/reference/cloudformation/package.html

<p align="center">____________________</p>

- A development team is considering Amazon ElastiCache for Redis as its in-memory caching solution for its relational database. Which of the following options are correct while configuring ElastiCache? (Select two)
    - If you have no replicas and a node fails, you experience no loss of data when using Redis with cluster mode enabled 
    - You can scale write capacity for Redis by adding replica nodes 
    - All the nodes in a Redis cluster must reside in the same region
    - While using Redis with cluster mode enabled, asynchronous replication mechanisms are used to keep the read replicas synchronized with the primary. If cluster mode is disabled, the replication mechanism is done synchronously 
    - While using Redis with cluster mode enabled, you cannot manually promote any of the replica nodes to primary

## Review Monitor and Troubleshooting
- An organization uses Alexa as its intelligent assistant to improve productivity throughout the organization. A group of developers manages custom Alexa Skills written in Node.Js to control conference-room equipment settings and start meetings using voice activation. The manager has requested developers that all functions code should be monitored for error rates with the possibility of creating alarms on top of them. Which of the following options should be chosen? (select two)
    - CloudTrail
    - CloudWatch Alarms
    - CloudWatch Metrics
    - X-Ray
    - SSM

https://aws.amazon.com/cloudwatch/

https://aws.amazon.com/cloudtrail/

https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html

<p align="center">____________________</p>

- Your company manages hundreds of EC2 instances running on Linux OS. The instances are configured in several Availability Zones in the eu-west-3 region. Your manager has requested to collect system memory metrics on all EC2 instances using a script. Which of the following solutions will help you collect this data?
    - Extract RAM statistics using the instance metadata
    - Extract RAM statistics from the standard CloudWatch metrics for EC2 instances
    - Use a cron job on the instances that pushes the EC2 RAM statistics as a Custom metric into CloudWatch
    - Extract RAM statistics using X-Ray

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/mon-scripts.html

## Review Development with AWS services
- Your mobile application needs to perform API calls to DynamoDB. You do not want to store AWS secret and access keys onto the mobile devices and need all the calls to DynamoDB made with a different identity per mobile device. Which of the following services allows you to achieve this?
    - Cognito Sync
    - IAM
    - Cognito Identity Pools
    - Cognito User Pools

 https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html


<p align="center">____________________</p>

- You are designing a high-performance application that requires millions of connections. You have several EC2 instances running Apache2 web servers and the application will require capturing the user’s source IP address and source port without the use of X-Forwarded-For. Which of the following options will meet your needs?
    - CLB
    - ALB
    - NLB
    - ELB

https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html

<p align="center">____________________</p>

- A developer is configuring an Application Load Balancer (ALB) to direct traffic to the application's EC2 instances and Lambda functions. Which of the following characteristics of the ALB can be identified as correct? (Select two)
    - If you specify targets using an instance ID, traffic is routed to instances using any private IP address from one or more network interfaces
    - If you specify targets using IP addresses, traffic is routed to instances using the primary private IP address
    - An ALB has three possible target types: Hostname, IP and Lambda
    - You can not specify publicly routable IP addresses to an ALB
    - An ALB has three possible target types: Instance, IP and Lambda

https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html

<p align="center">____________________</p>

- A .NET developer team works with many ASP.NET web applications that use EC2 instances to host them on IIS. The deployment process needs to be configured so that multiple versions of the application can run in AWS Elastic Beanstalk. One version would be used for development, testing, and another version for load testing. Which of the following methods do you recommend?
    - Use only one Beanstalk environment and perform configuration changes using an Ansible script
    - Create an Application Load Balancer to route based on hostname so you can pass on parameters to the development Elastic Beanstalk environment. Create a file in .ebextensions/ to know how to handle the traffic coming from the ALB
    - Define a dev environment with a single instance and a 'load test' environment that has settings close to production environment
    - You cannot have multiple development environments in Elastic Beanstalk, just one development, and one production environment

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.html

<p align="center">____________________</p>

- You have configured a Network ACL and a Security Group for the load balancer and Amazon EC2 instances to allow inbound traffic on port 80. However, users are still unable to connect to your website after launch. Which additional configuration is required to make the website accessible to all users over the internet?
    - Add a rule to the Network ACLs to allow outbound traffic on ports 1024 - 65535
    - Add a rule to the Network ACLs to allow outbound traffic on ports 1025 - 5000 
    - Add a rule to the Network ACLs to allow outbound traffic on ports 32768
    - Add a rule to the Security Group allowing outbound traffic on port 80

https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html

https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html

<p align="center">____________________</p>

- A firm maintains a highly available application that receives HTTPS traffic from mobile devices and web browsers. The main Developer would like to set up the Load Balancer routing to route traffic from web servers to smart.com/api and from mobile devices to smart.com/mobile. A developer advises that the previous recommendation is not needed and that requests should be sent to api.smart.com and mobile.smart.com instead. Which of the following routing options were discussed in the given use-case? (select two)
    - Host based
    - Cookie based
    - Client IP
    - Web browser version
    - Path based

https://aws.amazon.com/blogs/aws/new-host-based-routing-support-for-aws-application-load-balancers/