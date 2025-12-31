# Practice Test 2

- Score 76%
![PT 2 Results](../media/pt-2-results.png)

# ToDo list review:
- Security
    - ~~Signed urls and signed cookies in CloudFront~~
    - ~~Envelope encryption~~
- Refactoring
    - ~~Lambda functions App auto scaling~~
    - ~~Provisioned vs Reserved concurrency~~
    - ~~Spot instance interruptions~~
- Deployment
    - ~~Lambda and container images~~
    - ~~ASG Health checks~~
- Monitor and Troubleshooting
    - ~~CloudFormation parameter types.~~
- Review Development with AWS services
    - ~~DynamoDB atomic counters vs conditional writes vs transactions~~
    - ~~EBS storage types (focus on max size to IOPS ratios)~~
    - ~~DynamoDB backups~~
    - ~~Redshift~~

## Review Security
- The Development team at a media company is working on securing their databases. Which of the following AWS database engines can be configured with IAM Database Authentication? (Select two)
    - RDS MySQL
    - RDS Sequel Server
    - RDS PostGreSQL
    - Aurora
    - RDS Oracle

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html

<p align="center">____________________</p>

- A pharmaceutical company uses Amazon EC2 instances for application hosting and Amazon CloudFront for content delivery. A new research paper with critical findings has to be shared with a research team that is spread across the world. Which of the following represents the most optimal solution to address this requirement without compromising the security of the content?
    - Using CloudFront Field-Level Encryption to help protect sensitive data
    - Use CloudFront signed cookies feature to control access to the file
    -  Configure AWS Web Application Firewall (WAF) to monitor and control the HTTP and HTTPS requests that are forwarded to CloudFront
    - Use CloudFront signed URL feature to control access to the file.

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-signed-urls.html

<p align="center">____________________</p>

- A developer is defining the signers that can create signed URLs for their Amazon CloudFront distributions. Which of the following statements should the developer consider while defining the signers? (Select two)
    - CloudFront key pairs can be created with any account that has administrative permissions and full access to CloudFront resources.
    - When you use the root user to manage CloudFormation key pairs, you can only have up to two active ClodFront key pairs per AWS account.
    - You can also use AWS IAM permissions policies to restrict what the root user can do with CloudFront key pairs.
    - Both the signers (trust key group adn CloudFront key pairs) can be managed using the CloudFront API
    - When you create a signer, the public key is with CloudFront and private key is used to sign a portion of the URL.

<p align="center">____________________</p>

- A developer is looking at establishing access control for an API that connects to a Lambda function downstream. Which of the following represents a mechanism that CANNOT be used for authenticating with the API Gateway?
    - Cognito User Pools
    - Standard AWS IAM roles and policies
    - AWS STS
    - Lambda authorizer

https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html

<p align="center">____________________</p>

- A company runs its flagship application on a fleet of Amazon EC2 instances. After misplacing a couple of private keys from the SSH key pairs, they have decided to re-use their SSH key pairs for the different instances across AWS Regions. As a Developer Associate, which of the following would you recommend to address this use-case?
    - Encrypt the private SSH key and store ir int he S3 bucket to be accessed from any region
    - Generate a public SSH key pair from private SSH key. Then, import the key into each of your regions
    - Store the public and private SSH key pair in AWS Trusted Advisor and access it across regions
    - Its not possible to reuse SSH key pairs across regions

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html

<p align="center">____________________</p>

- You have launched several AWS Lambda functions written in Java. A new requirement was given that over 1MB of data should be passed to the functions and should be encrypted and decrypted at runtime. Which of the following methods is suitable to address the given use-case?
    - Use KMS direct encryption and store as a file
    - Use Envelope Encryption and store as an env variable
    - Use KMS encryption and store as an env variable
    - Use Envelope encryption and reference the data as a file within the code.

https://aws.amazon.com/es/kms/faqs/

## Review Refactoring

- The development team at a retail company is gearing up for the upcoming Thanksgiving sale and wants to make sure that the application's serverless backend running via Lambda functions does not hit latency bottlenecks as a result of the traffic spike. As a Developer Associate, which of the following solutions would you recommend to address this use-case?
    - Nop need to make andy special provisions as Lambda is automatically scalable because of its serverless architecture
    - Add an ALB in front of the lambda functions
    - Configure Application auto scaling to manage lambda provisioned concurrency
    - Configure Application auto scaling to manage Lambda reserved concurrency on a schedule.

https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html

<p align="center">____________________</p>

- A new recruit is trying to configure what an Amazon EC2 should do when it interrupts a Spot Instance. Which of the below CANNOT be configured as an interruption behavior?
    - Stop
    - Hibernate
    - Terminate
    - Reboot

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html

## Review Deployment

- A developer wants to package the code and dependencies for the application-specific Lambda functions as container images to be hosted on Amazon Elastic Container Registry (ECR). Which of the following options are correct for the given requirement? (Select two)
    - You can deploy Lambda function as a container image with a maximum size of 15 GB
    - Lambda supports both Windows and Linux-based images
    - You can test the containers locally using the Lambda Runtime API
    - To deploy a container image to Lambda, the container image must implement the Lambda Runtime API
    - You must create the Lambda function from the same account as the container registry in Amazon ECR.

https://docs.aws.amazon.com/lambda/latest/dg/images-create.html

<p align="center">____________________</p>

- You are a developer working on a web application written in Java and would like to use AWS Elastic Beanstalk for deployment because it would handle deployment, capacity provisioning, load balancing, auto-scaling, and application health monitoring. In the past, you connected to your provisioned instances through SSH to issue configuration commands. Now, you would like a configuration mechanism that automatically applies settings for you. Which of the following options would help do this?
    - Deploy a CloudFormation template
    - Use SSM parameter store as an input to your Elastic beanstalk configurations
    - Use lambda hook
    - Include config files in ./ebextensions at the root of your source code. 

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ebextensions.html

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ebextensions-optionsettings.html

## Review Monitor and Troubleshooting

- Your team lead has asked you to learn AWS CloudFormation to create a collection of related AWS resources and provision them in an orderly fashion. You decide to provide AWS-specific parameter types to catch invalid values. When specifying parameters which of the following is not a valid Parameter type?
    - CommaDelimitedList
    - AWS::EC2::KeyPair::KeyName
    - String
    - DependentParameter

https://aws.amazon.com/blogs/devops/using-the-new-cloudformation-parameter-types/

<p align="center">____________________</p>

- A development team has configured their Amazon EC2 instances for Auto Scaling. A Developer during routine checks has realized that only basic monitoring is active, as opposed to detailed monitoring. Which of the following represents the best root-cause behind the issue?
    - AWS Console might have been used to create the launch configuration
    - AWS CLI was used to create the launch configuration
    - The default configuration for Auto Scaling was not set
    - SDK was used to create the launch configurations

## Review Development with AWS services

- A development team is working on an AWS Lambda function that accesses DynamoDB. The Lambda function must do an upsert, that is, it must retrieve an item and update some of its attributes or create the item if it does not exist. Which of the following represents the solution with MINIMUM IAM permissions that can be used for the Lambda function to achieve this functionality?
    - dynamodb:GetRecords, dynamodb:PutItem, dynamodb:UpdateTable
    - dynamodb:UpdateItem, dynamodb:GetItem, dynamodb:PutItem
    - dynamodb:AddItem, dynamodb:GetItem
    - dynamodb:UpdateItem, dynamodb:GetItem

https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazondynamodb.html

<p align="center">____________________</p>

- A pharmaceutical company runs their database workloads on Provisioned IOPS SSD (io1) volumes. As a Developer Associate, which of the following options would you identify as an INVALID configuration for io1 EBS volume types?
    - 200 GiB size volume with 15000 IOPS
    - 200 GiB size volume with 2000 IOPS 
    - 200 GiB size volume with 10000 IOPS
    - 200 GiB size volume with 5000 IOPS

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html

<p align="center">____________________</p>

- A diagnostic lab stores its data on DynamoDB. The lab wants to backup a particular DynamoDB table data on Amazon S3, so it can download the S3 backup locally for some operational use. Which of the following options is NOT feasible?
    - Use AWS Data Pipeline to export your table to an S3 bucket in the account of your choice and download locally 
    - Use the DynamoDB on-demand backup capability to write to Amazon S3 and download locally
    - Use Hive with Amazon EMR to export your data to an S3 bucket and download locally
    - Use AWS Glue to copy your table to Amazon S3 and download locally

https://aws.amazon.com/premiumsupport/knowledge-center/back-up-dynamodb-s3/

<p align="center">____________________</p>

- A media publishing company is using Amazon EC2 instances for running their business-critical applications. Their IT team is looking at reserving capacity apart from savings plans for the critical instances. As a Developer Associate, which of the following reserved instance types you would select to provide capacity reservations?
    - Neither Regional Reserved Instances nor Zonal Reserved Instances 
    - Both Regional Reserved Instances and Zonal Reserved Instances 
    - Regional Reserved Instances 
    - Zonal Reserved Instances

<p align="center">____________________</p>

- A business has their test environment built on Amazon EC2 configured on General purpose SSD volume. At which gp2 volume size will their test environment hit the max IOPS?
    - 2.7 TiB
    - 10.6 TiB
    - 5.3 TiB
    - 16 TiB

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html

<p align="center">____________________</p>

- While defining a business workflow as state machine on AWS Step Functions, a developer has configured several states. Which of the following would you identify as the state that represents a single unit of work performed by a state machine?
    - .
    ```json
    "HelloWorld": {
        "Type": "Task",
        "Resource": "arn:aws:lambda:us-east-1:123456789012:function:HelloFunction",
        "Next": "AfterHelloWorldState",
        "Comment": "Run the HelloWorld Lambda function"
        }
    ```
    - .
    ```json
    "wait_until" : {
        "Type": "Wait",
        "Timestamp": "2016-03-14T01:59:00Z",
        "Next": "NextState"
        }
    ```
    - .
    ```json
    "No-op": {
        "Type": "Task",
        "Result": {
            "x-datum": 0.381018,
            "y-datum": 622.2269926397355
        },
        "ResultPath": "$.coords",
        "Next": "End"
    }
    ```
    - .
    ```json
    "FailState": {
        "Type": "Fail",
        "Cause": "Invalid response.",
        "Error": "ErrorA"
    }
    ```

https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-task-state.html

<p align="center">____________________</p>

- A developer with access to the AWS Management Console terminated an instance in the us-east-1a availability zone. The attached EBS volume remained and is now available for attachment to other instances. Your colleague launches a new Linux EC2 instance in the us-east-1e availability zone and is attempting to attach the EBS volume. Your colleague informs you that it is not possible and need your help. Which of the following explanations would you provide to them?
    - EBS volumes are AZ locked
    - EBS volumes are region locked
    - EBS volume is encrypted
    - The required IAM permissions are missing

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes.html

<p align="center">____________________</p>

- A social gaming application supports the transfer of gift vouchers between users. When a user hits a certain milestone on the leaderboard, they earn a gift voucher that can be redeemed or transferred to another user. The development team wants to ensure that this transfer is captured in the database such that the records for both users are either written successfully with the new gift vouchers or the status quo is maintained. Which of the following solutions represent the best-fit options to meet the requirements for the given use-case? (Select two)
    - Use the DynamoDB transactional read and write APIs on the table items as a single, all or nothing operation
    - Use Athena transactional read and write APIs on the table items as a single all-or-nothing operation
    - Complete both operations on Amazon RedShift in a single transaction block
    - Perform DynamoDB read and write operations with ConsistentRead parameter set to true
    - Complete both operations on RDS MySQL in a single transaction block

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/transactions.html

