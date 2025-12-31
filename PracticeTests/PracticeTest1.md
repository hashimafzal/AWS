# Practice Test 1

- Score 73%
![PT 1 Results](../media/pt-1-results.png)

# ToDo list review:
- Security  
    - ~~EC2 instance Purchase Options~~
    - ~~KMS CMK (A customer master key)~~
    - ~~Structure of IAM policy~~
    - ~~Review IAM in depth (ACL, resource-based policy, identity-based policy, AWS SCP, permission boundary)~~
    - ~~Difference between User Pools and Identity Pools (Cognito)~~
    - ~~Access Advisor Feature on IAM console, AWS Trusted Advisor, Access Analyzer , Amazon Inspector.~~
    - ~~Secrets Manager vs SSM Parameter Store~~
    - ~~Systems Manager~~
- Refactoring
    - ~~ECS step scaling vs target tracking policy~~
- Deployment
    - ~~Conditions in CF templates (the cant affect Parameter section)~~
    - ~~[Review CF Pseudo parameters](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/pseudo-parameter-reference.html)~~
    - ~~Managing failed deployments in EB~~
- Monitor and Troubleshooting
    -  [AWS Config](https://aws.amazon.com/config/)
    - ~~[ALB Access Logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html)~~
    - ~~[ALB request tracing](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-monitoring.html)~~
    - ~~[Cross zone load balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html)~~

## Review Security
- A cybersecurity firm wants to run their applications on single-tenant hardware to meet security guidelines. Which of the following is the MOST cost-effective way of isolating their Amazon EC2 instances to a single tenant?
    - Spot instance
    - Dedicated Host
    - On-Demand Instances
    - Dedicated Instance

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-overview.html#dedicated-hosts-dedicated-instances

<p align="center">____________________</p>

- In addition to regular sign-in credentials, AWS supports Multi-Factor Authentication (MFA) for accounts with privileged access. Which of the following MFA mechanisms is NOT for root user authentication?
    - Hardware MFA device
    - U2F security key
    - Virtual MFA device
    - SMS text message-based MFA

https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html

<p align="center">____________________</p>

- The development team has just configured and attached the IAM policy needed to access AWS Billing and Cost Management for all users under the Finance department. But, the users are unable to see AWS Billing and Cost Management service in the AWS console. What could be the reason for this issue?
    - You need to activate IAM user access to the Billing and Cost Management console for all the users who need access
    - IAM user should be created under AWS Billing and Cost Management and not under AWS accounts to have access to Billing console
    - The user might have another policy that restricts them from accessing Billing information
    - Only root user has access to AWS Billing and Cost Management console

https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/control-access-billing.html

<p align="center">____________________</p>

- A development team lead is configuring policies for his team at an IT company. Which of the following policy types only limit permissions but cannot grant permissions (Select two)?
    - ACL
    - Resource-based policy
    - AWS Organizations Service Control Policy (SCP)
    - Permissions boundary
    - Identity-based policy

https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html

<p align="center">____________________</p>

You are a developer for a web application written in .NET which uses the AWS SDK. You need to implement an authentication mechanism that returns a JWT (JSON Web Token). Which AWS service will help you with token handling and management?
    - Cognito User Pools
    - Cognito Sync
    - API Gateway
    - Cognito Identity Pools

https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html


<p align="center">____________________</p>

A developer is configuring a bucket policy that denies upload object permission to any requests that do not include the x-amz-server-side-encryption header requesting server-side encryption with SSE-KMS for an Amazon S3 bucket - examplebucket. Which of the following policies is the right fit for the given requirement?

https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html

<p align="center">____________________</p>

- To enable HTTPS connections for his web application deployed on the AWS Cloud, a developer is in the process of creating server certificate. Which AWS entities can be used to deploy SSL/TLS server certificates? (Select two)
    - AWS Certificate Manager
    - IAM
    - AWS Secrets Manager
    - AWS Systems Manager
    - AWS CloudFormation

https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html

<p align="center">____________________</p>

- A Developer has been entrusted with the job of securing certain S3 buckets that are shared by a large team of users. Last time, a bucket policy was changed, the bucket was erroneously available for everyone, outside the organization too. Which feature/service will help the developer identify similar security issues with minimum effort?
    - S3 Analytics
    - IAM Access Analyzer
    - Access Advisor feature on IAM console
    - S3 Object Lock

https://docs.aws.amazon.com/AmazonS3/latest/dev/security-best-practices.html
https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html

## Review Refactoring

- An e-commerce company has developed an API that is hosted on Amazon ECS. Variable traffic spikes on the application are causing order processing to take too long. The application processes orders using Amazon SQS queues. The ApproximateNumberOfMessagesVisible metric spikes at very high values throughout the day which triggers the CloudWatch alarm. Other ECS metrics for the API containers are well within limits. As a Developer Associate, which of the following will you recommend for improving performance while keeping costs low?
    - Use backlog per instance metric with target tracking scaling policy
    - Use docker swarm
    - Use EC2 service scheduler
    - Use ECS step scaling policy

https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html

## Review Deployment

- A Developer at a company is working on a CloudFormation template to set up resources. Resources will be defined using code and provisioned based on certain conditions. Which section of a CloudFormation template does not allow for conditions?
    - Resources
    - Conditions
    - Parameters
    - Outputs

<p align="center">____________________</p>

- You're a developer working on a large scale order processing application. After developing the features, you commit your code to AWS CodeCommit and begin building the project with AWS CodeBuild before it gets deployed to the server. The build is taking too long and the error points to an issue resolving dependencies from a third-party. You would like to prevent a build running this long in the future for similar underlying reasons. Which of the following options represents the best solution to address this use-case?
    - Enable CodeBuild Timeouts
    - Use VPC Flow Logs
    - Use AWS Lambda
    - USe AWS CloudWatch Events

 https://docs.aws.amazon.com/codebuild/latest/userguide/builds-working.html

<p align="center">____________________</p>

- After a test deployment in ElasticBeanstalk environment, a developer noticed that all accumulated Amazon EC2 burst balances were lost. Which of the following options can lead to this behavior?
    - The deploy was run as Rolling deployment, resulting in the resetting of EC2 burst balances
    - The deployment was run as all-at-once, flushing all the accumulated EC2 burst balance
    - The deployment was either run with immutable updates or in traffic splitting mode
    - When canary deployment fails, it resets the EC2 burst balance to zero

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.rolling-version-deploy.html

<p align="center">____________________</p>

- You have created a Java application that uses RDS for its main data storage and ElastiCache for user session storage. The application needs to be deployed using Elastic Beanstalk and every new deployment should allow the application servers to reuse the RDS database. On the other hand, user session data stored in ElastiCache can be re-created for every deployment. Which of the following configurations will allow you to achieve this? (Select two)
    - ElastiCache defined in .ebextensions/
    - RDS database defined in .ebextensions/
    - ElasticCache database defined externally and referenced through environment variables
    - RDS database defined externally and referenced through environment variables
    - ElastiCache bundled with the application source code.

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ebextensions.html

<p align="center">____________________</p>

- CodeCommit is a managed version control service that hosts private Git repositories in the AWS cloud. Which of the following credential types is NOT supported by IAM for CodeCommit?
    - Git credentials
    - AWS Access Keys
    - IAM username and password
    - SSH keys

<p align="center">____________________</p>

- When running a Rolling deployment in Elastic Beanstalk environment, only two batches completed the deployment successfully, while rest of the batches failed to deploy the updated version. Following this, the development team terminated the instances from the failed deployment. What will be the status of these failed instances post termination?
    - Elastic beanstalk will replace the failed instances after the application version to be installed ius manually chosen from the console
    - Elastic beanstalk will not replace failed instances.
    - Elastic beanstalk will replace the failed instances with instances running the application version from the oldest successful deployment
    - Elastic beanstalk will replace the failed instances with instances running the application version from the most recent successful deployment.

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.rolling-version-deploy.html

## Review Monitor and Troubleshooting

- A multi-national company has multiple business units with each unit having its own AWS account. The development team at the company would like to debug and trace data across accounts and visualize it in a centralized account. As a Developer Associate, which of the following solutions would you suggest for the given use-case?
    - VPC Flow logs
    - CloudTrail
    - X-Ray
    - CloudWatch events

 https://aws.amazon.com/xray/

<p align="center">____________________</p>

- An organization has offices across multiple locations and the technology team has configured an Application Load Balancer across targets in multiple Availability Zones. The team wants to analyze the incoming requests for latencies and the client's IP address patterns. Which feature of the Load Balancer will help collect the required information?
    - CW metrics
    - ALB request tracing
    - ALB access logs
    - CloudTrail logs

 https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html

## Review Development with AWS services

- An application is hosted by a 3rd party and exposed at yourapp.3rdparty.com. You would like to have your users access your application using www.mydomain.com, which you own and manage under Route 53. What Route 53 record should you create?
    - CNAME
    - PTR
    - Alias
    - A

https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-choosing-alias-non-alias.html

<p align="center">____________________</p>

- A multi-national company has just moved to AWS Cloud and it has configured forecast-based AWS Budgets alerts for cost management. However, no alerts have been received even though the account and the budgets have been created almost three weeks ago. What could be the issue with the AWS Budgets configuration?
    - CW could be down and hence alerts are not being sent.
    - Budget forecast has been created from an account that does not have enough privileges
    - AWS requires approximately 5 weeks of usage data to generate budget forecast.
    - Account hast to be part of AWS Organization to receive AWS Budgets alerts.

https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-best-practices.html

<p align="center">____________________</p>

- As part of his development work, an AWS Certified Developer Associate is creating policies and attaching them to IAM identities. After creating necessary Identity-based policies, he is now creating Resource-based policies. Which is the only resource-based policy that the IAM service supports?
    - Permission Boundary
    - AWS Organizations Service Control Policies (SCP)
    - ACL
    - Trust policy

https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_resource-based

https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html

<p align="center">____________________</p>

- A startup with newly created AWS account is testing different EC2 instances. They have used Burstable performance instance - T2.micro - for 35 seconds and stopped the instance. At the end of the month, what is the instance usage duration that the company is charged for?
    - 30 seconds
    - 35 seconds
    - 60 seconds
    - 0 seconds