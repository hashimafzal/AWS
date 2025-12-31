# Practice Test 3

- Score 78%
![PT Results 3](../media/pt-3-results.png)

# ToDo list review:
- Security
    - ~~KMS~~
    - ~~AWS Partitions~~
- Refactoring
    - ~~AWS Web Application Firewall~~
    - ~~HTTP API vs REST API~~
- Deployment
    - ~~Deployment types for code deploy~~
- Monitor and Troubleshooting
    - ~~AWS Organizations Trails~~
- Review Development with AWS services
    - ~~ASG vs EC2 enable detailed monitoring CLI~~
    - ~~Express Workflows vs Standard Workflows~~
    - ~~S3 replication~~

## Review Security
- Your application is deployed automatically using AWS Elastic Beanstalk. Your YAML configuration files are stored in the folder .ebextensions and new files are added or updated often. The DevOps team does not want to re-deploy the application every time there are configuration changes, instead, they would rather manage configuration externally, securely, and have it load dynamically into the application at runtime. What option allows you to do this?
    - Env variables
    - Use stage variables
    - Use S3
    - Use SSM Parameter store

https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-paramstore.html

<p align="center">____________________</p>

- A large firm stores its static data assets on Amazon S3 buckets. Each service line of the firm has its own AWS account. For a business use case, the Finance department needs to give access to their S3 bucket's data to the Human Resources department. Which of the below options is NOT feasible for cross-account access of S3 bucket objects?
    - Use IAM roles and resource-based policies delegate access across accounts with different partitions via programmatic access only.
    - Use SCL adn IAM policies for programmatic-only access to s3 bucket objects
    - USe cross-account IAM roles fro programmatic and console access to S3 bucket objects
    - Use Resource-based policies and AWS IAM policies for programmatic-only access to s3 bucket objects.

https://docs.aws.amazon.com/AmazonS3/latest/dev/example-walkthroughs-managing-access-example3.html

https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html

https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_compare-resource-policies.html

https://aws.amazon.com/premiumsupport/knowledge-center/cross-account-access-s3/

<p align="center">____________________</p>

- A financial services company wants to ensure that the customer data is always kept encrypted on Amazon S3 but wants a fully managed solution to create, rotate and remove the encryption keys. As a Developer Associate, which of the following would you recommend to address the given use-case?
    - Server-side encryption with CMKs stored in AWS KMS (SSE-KMS)
    - Server side encryption with Amazon S3-Managed Keys (SSE-S3)
    - Server-side encryption with Customer-provided keys (SSE-C)
    - Server side encryption with Secrets Manager

https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingKMSEncryption.html

## Review Refactoring
- You company runs business logic on smaller software components that perform various functions. Some functions process information in a few seconds while others seem to take a long time to complete. Your manager asked you to decouple components that take a long time to ensure software applications stay responsive under load. You decide to configure Amazon Simple Queue Service (SQS) to work with your Elastic Beanstalk configuration. Which of the following Elastic Beanstalk environment should you choose to meet this requirement?
    - Dedicated worker environment
    - Single instance with Elastic IP
    - Single instance Worker node
    - Load-balancing, Autoscaling environment

<p align="center">____________________</p>

- A developer is configuring an Amazon API Gateway as a front door to expose backend business logic. To keep the solution cost-effective, the developer has opted for HTTP APIs. Which of the following services are not available as an HTTP API via Amazon API Gateway?
    - AWS Web Application Firewall 
    - Lambda
    - IAM
    - Cognito

https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html

<p align="center">____________________</p>

- As a Senior Developer, you manage 10 Amazon EC2 instances that make read-heavy database requests to the Amazon RDS for PostgreSQL. You need to make this architecture resilient for disaster recovery. Which of the following features will help you prepare for database disaster recovery? (Select two)
    - Use cross-Region Read Replicas
    - Enable the automated backup feature in RDS in a multi-AZ deployment that creates backups in a single AWS region
    - Use RDS Provisioned IOPS (SSD) Storage in place of General Purpose (SSD) Storage.
    - Use database cloning feature of RDS DB cluster
    - Enable the automated backup feature of Amazon RDS in a multi-*AZ deployment that creates backups across multiple regions.

## Review Deployment

- You have a workflow process that pulls code from AWS CodeCommit and deploys to EC2 instances associated with tag group ProdBuilders. You would like to configure the instances to archive no more than two application revisions to conserve disk space. Which of the following will allow you to implement this?
    - Have a load balancer in front of your instances
    - AWS CW Log Agent
    - Integrate wit CodePipeline
    - CodeDeploy Agent

https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent.html

https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AgentReference.html

## Review Monitor and Troubleshooting
- You are working for a shipping company that is automating the creation of ECS clusters with an Auto Scaling Group using an AWS CloudFormation template that accepts cluster name as its parameters. Initially, you launch the template with input value 'MainCluster', which deployed five instances across two availability zones. The second time, you launch the template with an input value 'SecondCluster'. However, the instances created in the second run were also launched in 'MainCluster' even after specifying a different cluster name. What is the root cause of this issue?
    - The ECS agent docker image must be reinstalled to connect to the other clusters
    - The EC2 instance is missing IAM permissions to join the other clusters
    - The cluster name Parameter has not been updated in the file /etc/ecs/ecs.config during bootstrap
    - The SG of EC2 instances are pointing to the wrong ECS cluster.

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/bootstrap_container_instance.html

<p align="center">____________________</p>

- A junior developer working on ECS instances terminated a container instance in Amazon Elastic Container Service (Amazon ECS) as per instructions from the team lead. But the container instance continues to appear as a resource in the ECS cluster. As a Developer Associate, which of the following solutions would you recommend to fix this behavior?
    - You terminated the container instance while it was STOPPED state, that lead to this synchronization error.
    - A custom software on the container instance could have failed and resulted in the container hanging in an unhealthy state until restarted again.
    - The container instance has been terminated with AWS CLI, whereas, for ECS instances, Amazon ECS CLI should be used to avoid any synchronization issues
    - You terminated the container instance while it was in RUNNING state, that lead to the synchronization issues.

<p align="center">____________________</p>

- An IT company has migrated to a serverless application stack on the AWS Cloud with the compute layer being implemented via Lambda functions. The engineering managers would like to actively troubleshoot any failures in the Lambda functions. As a Developer Associate, which of the following solutions would you suggest for this use-case?
    - Use CW events to identify and notify any failures in the lambda code
    - Use CodeCommit to identify and notify any failures in Lambda code
    - Use CodeDeploy to identify and notify any failures in the Lambda code
    - The developers should insert logging statements in Lambda function code which are then available in CW logs.

https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html

<p align="center">____________________</p>

- A multi-national enterprise uses AWS Organizations to manage its users across different divisions. Even though CloudTrail is enabled on the member accounts, managers have noticed that access issues to CloudTrail logs across different divisions and AWS Regions is becoming a bottleneck in troubleshooting issues. They have decided to use the organization trail to keep things simple. What are the important points to remember when configuring an organization trail? (Select two)
    - There is nothing called Organization Trail. The master account can, however, enable CloudTrail logging, to keep track of all activities across AWS accounts 
    - Member accounts will be able to see the organization trail, but cannot modify or delete it
    - By default, CloudTrail tracks only bucket-level actions. To track object-level actions, you need to enable Amazon S3 data events
    - Member accounts do not have access to the organization trail, neither do they have access to the Amazon S3 bucket that logs the files 
    - By default, CloudTrail event log files are not encrypted -

https://docs.aws.amazon.com/awscloudtrail/latest/userguide/how-cloudtrail-works.html

https://aws.amazon.com/about-aws/whats-new/2016/11/aws-cloudtrail-supports-s3-data-events/

https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/

<p align="center">____________________</p>

- A telecommunications company that provides internet service for mobile device users maintains over 100 c4.large instances in the us-east-1 region. The EC2 instances run complex algorithms. The manager would like to track CPU utilization of the EC2 instances as frequently as every 10 seconds. Which of the following represents the BEST solution for the given use-case?
    - Create a high-resolution custom metric and push the data using a script triggered every 10 seconds
    - Enable EC2 detailed monitoring
    - Simply get it from the CloudWatch Metrics 
    - Open a support ticket with AWS 

https://aws.amazon.com/blogs/aws/new-high-resolution-custom-metrics-and-alarms-for-amazon-cloudwatch/

## Review Development with AWS services
- The development team at a company wants to encrypt a 111 GB object using AWS KMS. Which of the following represents the best solution?
    - Make a GenerateDataKey API call that returns a plaintext key and an encrypted copy of a data key. Use a plaintext key to encrypt the data 
    - Make a GenerateDataKeyWithPlaintext API call that returns an encrypted copy of a data key. Use a plaintext key to encrypt the data
    - Make an Encrypt API call to encrypt the plaintext data as ciphertext using a customer master key (CMK) with imported key material 
    - Make a GenerateDataKeyWithoutPlaintext API call that returns an encrypted copy of a data key. Use an encrypted key to encrypt the data

https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html

https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html

https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html

<p align="center">____________________</p>

- The development team at a social media company is considering using Amazon ElastiCache to boost the performance of their existing databases. As a Developer Associate, which of the following use-cases would you recommend as the BEST fit for ElastiCache? (Select two)
    - Use ElastiCache to improve latency and throughput for read-heavy application workloads
    - Use ElastiCache to improve performance of compute-intensive workloads
    - Use ElastiCache to improve latency and throughput for write-heavy application workloads 
    - Use ElastiCache to improve performance of Extract-Transform-Load (ETL) workloads
    - Use ElastiCache to run highly complex JOIN queries 

https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/elasticache-use-cases.html

https://aws.amazon.com/elasticache/features/

<p align="center">____________________</p>

- A development team uses shared Amazon S3 buckets to upload files. Due to this shared access, objects in S3 buckets have different owners making it difficult to manage the objects. As a developer associate, which of the following would you suggest to automatically make the S3 bucket owner, also the owner of all objects in the bucket, irrespective of the AWS account used for uploading the objects?
    - Use S3 Object Ownership to default bucket owner to be the owner of all objects in the bucket
    - Use S3 CORS to make the S3 bucket owner, the owner of all objects in the bucket
    - Use S3 Access Analyzer to identify the owners of all objects and change the ownership to the bucket owner 
    - Use Bucket Access Control Lists (ACLs) to control access on S3 bucket and then define its owner

https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html

https://docs.aws.amazon.com/AmazonS3/latest/userguide/cors.html

<p align="center">____________________</p>

- You have been asked by your Team Lead to enable detailed monitoring of the Amazon EC2 instances your team uses. As a Developer working on AWS CLI, which of the below command will you run?
    - aws ec2 run-instances --image-id ami-09092360 --monitoring Enabled=true
    - aws ec2 run-instances --image-id ami-09092360 --monitoring State=enabled
    - aws ec2 monitor-instances --instance-id i-1234567890abcdef0
    - aws ec2 monitor-instances --instance-ids i-1234567890abcdef0

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-new.html

https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html

<p align="center">____________________</p>

- To meet compliance guidelines, a company needs to ensure replication of any data stored in its S3 buckets. Which of the following characteristics are correct while configuring an S3 bucket for replication? (Select two)
    - Replicated objects do not retain metadata
    - Once replication is enabled on a bucket, all old and new objects will be replicated 
    - Object tags cannot be replicated across AWS Regions using Cross-Region Replication
    - S3 lifecycle actions are not replicated with S3 replication
    - Same-Region Replication (SRR) and Cross-Region Replication (CRR) can be configured at the S3 bucket level, a shared prefix level, or an object level using S3 object tags 

https://docs.amazonaws.cn/en_us/AmazonS3/latest/userguide/replication.html