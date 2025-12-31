# Practice Test 11

- Score 89%
![PT 11 Results](../media/pt-11-results.png)

# ToDo list review:
- Security
- Refactoring
- Deployment
- Monitor and Troubleshooting
- Review Development with AWS services


## Review Security
- A company is currently in the process of integrating their on-premises data center to their cloud infrastructure in AWS. One of the requirements is to integrate the on-premises Lightweight Directory Access Protocol (LDAP) directory service to their AWS VPC using IAM. Which of the following provides the MOST suitable solution to implement if the identity store that they are using is not compatible with SAML?
    - Creating IAM roles to rotate the IAM credentials whenever LDAP credentials are updated 
    - Implementing the AWS Single Sign-On (SSO) service to enable single sign-on between AWS and your LDAP is incorrect
    - Setting up an IAM policy that references the LDAP identifiers and AWS credentials
    - Create a custom identity broker application in your on-premises data center and use STS to issue short-lived AWS credentials.

https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.html

https://aws.amazon.com/blogs/aws/aws-identity-and-access-management-now-with-identity-federation/

https://www.youtube.com/watch?v=AIdUw0i8rr0

https://tutorialsdojo.com/aws-identity-and-access-management-iam/

<p align="center">____________________</p>

- A web application is currently using an on-premises Microsoft SQL Server 2019 Enterprise Edition database. Your manager instructed you to migrate the application to Elastic Beanstalk and the database to RDS. For additional security, you must configure your database to automatically encrypt data before it is written to storage, and automatically decrypt data when the data is read from storage. Which of the following services will you use to achieve this?
    - Enable RDS Encryption
    - Use Microsoft SQL Server Windows Authentication
    - Use IAM DB Authentication
    - Enable Transparent Data Encryption (TDE)

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.TDE.html

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html

https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/

<p align="center">____________________</p>

- You work for a software development company where the teams are divided into distinct projects. The management wants to have separation on their AWS resources, which will have a detailed report on the costs of each project. Which of the following options is the recommended way to implement this?
    - Creating separate AWS accounts for each project and generating Detailed Billing for each account
    - Tag resources by projects and use Detailed Billing Reports to show costing per tag
    - Create separate AWS accounts for each project and use consolidated billing
    - Tag resources by IAM group assigned for each project and use Detailed Billing reports to show costing

https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/DetailedBillingReport.html

http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html

https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/reportstagsresources.html

https://tutorialsdojo.com/aws-billing-and-cost-management/

## Review Refactoring

## Review Deployment

- An aerospace engineering company has recently migrated to AWS for their cloud architecture. They are using CloudFormation and AWS SAM as deployment services for both of their monolithic and serverless applications. There is a new requirement where you have to dynamically install packages, create files, and start services on your EC2 instances upon the deployment of the application stack using CloudFormation. Which of the following helper scripts should you use in this scenario?
    - cfn-init
    - cfn-signal
    - cfn-get-metadata
    - cfn-hup

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-init.html

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-helper-scripts-reference.html

https://s3.amazonaws.com/cloudformation-examples/BoostrappingApplicationsWithAWSCloudFormation.pdf

https://tutorialsdojo.com/aws-cloudformation/

## Review Monitor and Troubleshooting
- An application is hosted in an Auto Scaling group of EC2 instances behind an Application Load Balancer. You want to automatically monitor the CPU Utilization of each and every instances of your application stack throughout the day using Amazon CloudWatch. In this scenario, what is the time period of data that CloudWatch receives and aggregates from EC2 by default?
    - 1 second
    - 1 minute
    - 15 minutes
    - 5 minutes

https://aws.amazon.com/cloudwatch/faqs/

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-cloudwatch-new.html

https://tutorialsdojo.com/amazon-cloudwatch/

<p align="center">____________________</p>

- A company has an application hosted in an ECS Cluster which is heavily using an RDS database. A developer needs to closely monitor how the different processes on a DB instance use the CPU such as the percentage of the CPU bandwidth or the total memory consumed by each process to ensure application performance. Which of the following is the MOST suitable solution that the developer should implement?
    - Developing a shell script that collects and publishes custom metrics to CloudWatch which tracks the real-time CPU Utilization of the RDS instance
    - Using CloudWatch to track the CPU Utilization of your database
    - Tracking the CPU% and MEM% metrics which are readily available in the Amazon RDS console
    - Use Enhanced Monitoring in RDS

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html#USER_Monitoring.OS.CloudWatchLogs

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MonitoringOverview.html#monitoring-cloudwatch

https://tutorialsdojo.com/amazon-cloudwatch/

https://tutorialsdojo.com/amazon-relational-database-service-amazon-rds/

<p align="center">____________________</p>

- A web application hosted in Elastic Beanstalk has a configuration file named .ebextensions/debugging.config which has the following content:
For its database tier, it uses RDS with Multi-AZ deployments configuration and Read Replicas. There is a new requirement to record calls that your application makes to RDS and other internal or external HTTP web APIs. The tracing information should also include the actual SQL database queries sent by the application, which can be searched using the filter expressions in the X-Ray Console. Which of the following should you do to satisfy the above task?
    - Adding annotations in the subsegment section of the segment document
    - Adding annotations in the segment document
    - Adding metadata in the segment document
    - Adding metadata in the subsegment section of the segment document 

```yaml
option_settings: 
 aws:elasticbeanstalk:xray: 
  XRayEnabled: true
```

https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html#xray-concepts-annotations

https://docs.aws.amazon.com/xray/latest/devguide/xray-console-filters.html

https://tutorialsdojo.com/aws-x-ray/

<p align="center">____________________</p>

- A developer uses AWS X-Ray to create a trace on an instrumented web application and gain insights on how to better optimize its performance. The segment documents being sent by the application contain annotations which the developer wants to utilize in order to identify and filter out specific data from the trace. Which of the following should the developer do in order to satisfy this requirement with minimal configuration? (Select TWO.)
    - Using filter expressions via the X-Ray console and fetching the trace IDs and annotations using the GetTraceSummaries API
    - Fetching the data using the BatchGetTraces API
    - Sending trace results to an S3 bucket then querying the trace output using Amazon Athena
    - Configuring Sampling Rules in the AWS X-Ray Console

https://docs.aws.amazon.com/xray/latest/devguide/xray-console-filters.html

https://docs.aws.amazon.com/xray/latest/devguide/xray-api-segmentdocuments.html

https://docs.aws.amazon.com/xray/latest/api/API_GetTraceSummaries.html

https://tutorialsdojo.com/aws-x-ray/

## Review Development with AWS services
- You are configuring the task definitions of your ECS Cluster in AWS to make sure that the tasks are scheduled on instances with enough resources to run them. It should also follow the constraints that you specified both implicitly or explicitly. Which of the following options should you implement to satisfy the requirement which requires the LEAST amount of configuration?
    - Using a binpack task placement strategy 
    - Using a spread task placement strategy which uses the instanceId and host attributes
    - Use a random task placement strategy
    - Using a spread task placement strategy with custom placement constraints

https://aws.amazon.com/blogs/compute/amazon-ecs-task-placement/

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement.html

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html

https://tutorialsdojo.com/amazon-elastic-container-service-amazon-ecs/

<p align="center">____________________</p>

- Your new web app is running on several on-demand EC2 instances behind a Classic Load Balancer. One of your EC2 instances has failed the health check and is no longer receiving traffic. After manually rebooting the instance, the application check becomes healthy again. Which of the following steps will you do next?
    - Updating the health check again to re-scan and see which instances are healthy
    - Enabling Sticky Session on the ELB to rebalance traffic 
    - Restarting the classic load balancer to refresh the traffic flow 
    - Do nothing as the ELB will direct traffic to it after the health check threshold is passed

http://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html

https://www.youtube.com/watch?v=UBl5dw59DO8

https://tutorialsdojo.com/aws-elastic-load-balancing-elb/

https://tutorialsdojo.com/ec2-instance-health-check-vs-elb-health-check-vs-auto-scaling-and-custom-health-check/

<p align="center">____________________</p>

- You are designing the DynamoDB table that will be used by your Node.js application. It will have to handle 10 writes per second and then 20 eventually consistent reads per second where all the items have a size of 2 KB for both operations. Which of the following are the most optimal WCU and RCU that you should provision to the table?
    - 20 RCU and 20 WCU
    - 40 RCU and 20 WCU
    - 40 RCU and 40 WCU
    - 10 RCU and 20 WCU

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughput.html#ItemSizeCalculations.Writes

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.html

https://tutorialsdojo.com/amazon-dynamodb/

https://tutorialsdojo.com/calculating-the-required-read-and-write-capacity-unit-for-your-dynamodb-table/

<p align="center">____________________</p>

- You are working as an IT Consultant for a top investment bank in Europe which uses several serverless applications in their AWS account. They just launched a new API Gateway service with a Lambda proxy integration and you were instructed to test out the new API. However, you are getting a Connection refused error whenever you use this Invoke URL http://779protaw8.execute-api.us-east-1.amazonaws.com/tutorialsdojo/ of the API Gateway. Which of the following is the MOST likely cause of this issue?
    - You are not using FTP in invoking the API 
    - You are not using HTTP/2 in invoking the API 
    - You are not using HTTPS in invoking the API.
    - You are not using WebSocket in invoking the API

https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-call-api.html

https://aws.amazon.com/api-gateway/faqs/

https://tutorialsdojo.com/amazon-api-gateway/

<p align="center">____________________</p>

- You were recently hired by a media company that is planning to build a news portal using Elastic Beanstalk and DynamoDB database, which already contains a few data. There is already an existing DynamoDB Table that has an attribute of ArticleName which acts as the partition key and a Category attribute as its sort key. You are instructed to develop a feature that will query the ArticleName attribute but will use a different sort key other than the existing one. The feature also requires strong read consistency to fetch the most up-to-date data. Which of the following solutions should you implement?
    - Creating a Local Secondary Index that uses the ArticleName attribute and a different sort key
    - Creating a Global Secondary Index which uses the ArticleName attribute and your alternative sort key as projected attributes
    - Creating a Global Secondary Index that uses the ArticleName attribute and a different sort key
    - Create a new DynamoDB table with a Local Secondary Index that uses the ArticleName attribute with a different sort key then migrate the data from the existing table to the new table.

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LSI.html

https://tutorialsdojo.com/global-secondary-index-vs-local-secondary-index/

https://tutorialsdojo.com/aws-certified-developer-associate/

<p align="center">____________________</p>