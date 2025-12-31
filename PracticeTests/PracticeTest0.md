# Practice Test 0

# [Questions Link](https://www.whizlabs.com/blog/aws-developer-associate-exam-questions/)

What is used in S3 to enable client web applications that are loaded in one domain to interact with resources of the different domain? Choose the correct answer from the options below
A. CORS Configuration
B. Public Object Permissions
C. Public ACL Permissions
D. None of the above

Answer: A

Explanation: Cross-origin resource sharing (CORS) configuration is a way to interact with resources in a different domain for the client web applications loaded in one domain. With CORS, you can build client-side web applications with Amazon S3 and also allow cross-origin to have access to the S3 resources selectively.

<p align="center">____________________</p>

Which of the descriptions below best describes what the following bucket policy does?
{  
   “Version”:”2012-10-17″,
   “Id”:”Statement1”, 
   “Statement”:[  
      {  
         “Sid”:” Statement2″,
         “Effect”:”Allow”,
         “Principal”:”*”,
         “Action”:[  
            “s3:GetObject”,
            “s3:PutObject”
         ],
         “Resource”:”arn:aws:s3:::mybucket/*”,
         “Condition”:{  
            “StringLike”:{  
               “aws:Referer”:[  
                  “http://www.example.com/*”,
                  “http://www.demo.com/*”
               ]
            }
         }
      }
   ]
}

Choose the correct answer from the options below
A. It allows read or write actions on the bucket ‘mybucket’
B. It allows read access to the bucket ‘mybucket’ but only if it is accessed from example.com or demo.com
C. It allows unlimited access to the bucket ‘mybucket’
D. It allows read or write access to the bucket ‘mybucket’ but only if it is accessed from example.com or demo.com

Answer: D
Explanation: The PutObject allows one to put objects in an S3 bucket.

<p align="center">____________________</p>

Is the default visibility timeout for an SQS queue 1 minute?
A. True
B. False

Answer: B
Explanation: The visibility timeout of each queue is 30 seconds by default. It is possible to change this setting for all the queues. Typically, the visibility timeout is set to the average time it takes in processing and deleting a message from the queue. While receiving messages, special visibility timeout can be set for the returned messages without making any change in the overall timeout of the queue

<p align="center">____________________</p>

When a failure occurs during stack creation in Cloudformation, does a rollback occur?
A. True
B. False

Answer: A

Explanation: By default, the “automatic rollback on error” feature is enabled. It causes AWS CloudFormation to be created successfully for a stack until the point of error is deleted. This is useful when the default limit for Elastic IP addresses is exceeded accidentally, or you can’t access an EC2 AMI you want to run.

This feature makes you depend on the fact that stacks may either be fully created or not at all. It simplifies the layered solutions system administration built on the top of the AWS CloudFormation.

<p align="center">____________________</p>

An administrator is getting an error while trying to create a new bucket in S3? You feel that bucket limit has been crossed. What is the bucket limit per account in AWS? Choose the correct answer from the options below
A. 100
B. 50
C. 1000
D. 150

Answer: A
Explanation: This is clearly mentioned in the AWS documentation.

<p align="center">____________________</p>

Which of the below functions is used in Cloudformation to retrieve an object from a set of objects? Choose an answer from the options below
A. Fn::GetAtt
B. Fn::Combine
C. Fn::Join
D. Fn::Select

Answer: D
Explanation: This is clearly given in the AWS documentation

<p align="center">____________________</p>

Which of the below functions is used in Cloudformation to append a set of values into a single value? Choose an answer from the options below
A. Fn::GetAtt
B. Fn::Combine
C. Fn::Join
D. Fn::Select

Answer: C
Explanation: This is clearly given in the AWS documentation

<p align="center">____________________</p>

What is the max size of an item that corresponds to a single write capacity unit? (While creating an index or table in Amazon DynamoDB, it is required to specify the capacity requirements for the read and write activity)?.
Choose an answer from the options below.
A. 1 KB
B. 4 KB
C. 2 KB
D. 8 KB

Answer: A
Explanation: This is clearly given in the AWS documentation

<p align="center">____________________</p>

What can be used in DynamoDB as a part of the Query API call for the filtration of results based on the primary keys’ values? Choose an answer from the options below
A. Expressions
B. Conditions
C. Query API
D. Scan API

Answer: A
Explanation: This is clearly provided in the AWS documentation

<p align="center">____________________</p>

Can a global secondary index create at the same time as the table creation?
A. True
B. False

Answer: A
Explanation: This is clearly given in the AWS documentation

<p align="center">____________________</p>

A Global Secondary Index can have a different partition key and sort key from those of its base table. 
A. True
B. False

Answer: A
Explanation: GSI can also use the same partition key as the base table. Even in the AWS documentation, they say that GSI can use a different partition key and sort key. However, anywhere in the document, they are not saying that it has to be different.

<p align="center">____________________</p>

What in AWS can be used to restrict access to SWF?
A. ACL
B. SWF Roles
C. IAM
D. None of the above

Answer: C
Explanation: This is clearly mentioned in the AWS documentation

<p align="center">____________________</p>

An IT admin has enabled long polling in their SQS queue. What must be done for long polling to be enabled in SQS? Choose the correct answer from the options below
A. Create a dead letter queue
B. Set the message size to 256KB
C. Set the ReceiveMessageWaitTimeSeconds property of the queue to 0 seconds
D. Set the ReceiveMessageWaitTimeSeconds property of the queue to 20 seconds

Answer: D
Explanation: Amazon SQS long polling is a method of retrieval of messages from SQS queues. It returns a response only when a message arrives in the message queue instead of short polling where the response returns immediately even when the message is empty.
As the messages are available, the retrieval of messages from Amazon SQS becomes inexpensive due to long polling. It may also reduce the cost of using SQS as it can reduce the empty receipts.

<p align="center">____________________</p>

As per the IAM decision logic, what is the first step of access permissions for any resource in AWS? Choose the correct answer from the options below
A. A default deny
B. An explicit deny
C. An allow
D. An explicit allow

Answer: A
The below diagram shows the evaluation logic of IAM policies. And as per the evaluation logic, it is clear that the above scenario leads to a default deny.

![IAM evaluation Logic](../media/iam-evaluation-logic.png)

<p align="center">____________________</p>

Which API call is used to Bundle an Amazon instance store-backed Windows instance? Choose the correct answer from the options below
A. AllocateInstance
B. CreateImage
C. BundleInstance
D. ami-register-image

Answer: C
Explanation: This is given in the AWS documentation

<p align="center">____________________</p>

## Domain : Development with AWS Services

A developer is building an application that needs access to an S3 bucket. An IAM role is created with the required permissions to access the S3 bucket. Which API call should the Developer use in the application so that the code can access to the S3 bucket?
A. IAM: AccessRole
B. STS: GetSessionToken
C. IAM:GetRoleAccess
D. STS:AssumeRole

Correct Answer: D
Explanation: This is given in the AWS Documentation.
A role specifies a set of permissions that you can use to access AWS resources. In that sense, it is similar to an IAM user. An application assumes a role to receive permissions to carry out required tasks and interact with AWS resources. The role can be in your own account or any other AWS account. For more information about roles, their benefits, and how to create and configure them, see IAM Roles, and Creating IAM Roles. To learn about the different methods that you can use to assume a role, see Using IAM Roles.

Important: The permissions of your IAM user and any roles that you assume are not cumulative. Only one set of permissions is active at a time. When you assume a role, you temporarily give up your previous user or role permissions and work with the permissions assigned to the role. When you exit the role, your user permissions are automatically restored.

To assume a role, an application calls the AWS STS AssumeRole API operation and passes the ARN of the role to use. When you call AssumeRole, you can optionally pass a JSON policy. This allows you to restrict permissions for that for the role’s temporary credentials. This is useful when you need to give the temporary credentials to someone else. They can use the role’s temporary credentials in subsequent AWS API calls to access resources in the account that owns the role. You cannot use the passed policy to grant permissions that are in excess of those allowed by the permissions policy of the role that is being assumed. To learn more about how AWS determines the effective permissions of a role, see Policy Evaluation Logic.

Option A is incorrect because IAM does not have this API.
Option B is incorrect because STS:GetSessionToken is used if you want to use MFA to protect programmatic calls to specific AWS API operations like Amazon EC2 StopInstances. MFA-enabled IAM users would need to call GetSessionToken and submit an MFA code associated with their MFA device.
Option C is incorrect because IAM does not have this API.

STS stands for Security Token Service.

<p align="center">____________________</p>

A company is writing a Lambda function that will run in multiple stages, such a dev, test, and production. The function is dependent upon several external services, and it must call different endpoints for these services based on the function’s deployment stage.
What Lambda feature will enable the developer to ensure that the code references the correct endpoints when running in each stage?
A. Tagging
B. Concurrency
C. Aliases
D. Environment variables

Correct Answer: D
Explanation: You can create different environment variables in the Lambda function that can be used to point to the different services. The below screenshot from the AWS Documentation shows how this can be done with databases.

Option C is invalid since this is used for managing the different versions of your Lambda function.

<p align="center">____________________</p>

You are using S3 buckets to store images. These S3 buckets invoke a lambda function on upload. The Lambda function creates thumbnails of the images and stores them in another S3 bucket. An AWS CloudFormation template is used to create the Lambda function with the resource “AWS::Lambda::Function”. Which of the following attributes is the method name that Lambda calls to execute the function?
Sample CloudFormation template:

![QA 1](../media/qa-1.png)

A. Function Name
B. Layers
C. Environment
D. Handler

Correct Answer: D
Explanation: The handler is the name of the method within a code that Lambda calls to execute the function.

Option A is incorrect as the version number changes when the functions are “published”, so FunctionName is incorrect.
Option B is incorrect as it’s a list of function layers added to the Lambda function execution environment.
Option C is incorrect as these are variables that are accessible during Lambda function execution.

<p align="center">____________________</p>

Your application is developed to pick up metrics from several servers and push them off to CloudWatch. At times, the application gets client 429 errors. Which of the following can be done from the programming side to resolve such errors?
A. Use the AWS CLI instead of the SDK to push the metrics
B. Ensure that all metrics have a timestamp before sending them across
C. Use exponential backoff in your requests
D. Enable encryption for the requests

Correct Answer: C

Explanation: 429 code is "Too Much Requests". The main reason for such errors is that throttling occurs when many requests are sent via API calls. The best way to mitigate this is to stagger the rate at which you make the API calls.

In addition to simple retries, each AWS SDK implements an exponential backoff algorithm for better flow control. The idea behind exponential backoff is to use progressively longer waits between retries for consecutive error responses. You should implement a maximum delay interval, as well as a maximum number of retries. The maximum delay interval and maximum number of retries are not necessarily fixed values and should be set based on the operation being performed and other local factors, such as network latency.

Option A is invalid because this accounts for the same thing. It’s basically the number of requests that is the issue.
Option B is invalid because any way you have to add the timestamps when sending the requests.
Option D is invalid because this would not help in the issue.

<p align="center">____________________</p>

You are a developer for your company. You are working on creating Cloudformation templates for different environments. You want to be able to base the creation of the environments on the values passed at runtime to the template. How can you achieve this?
A. Specify an Outputs section
B. Specify a parameters section
C. Specify a metadata section
D. Specify a transform section

Correct Answer: B
Explanation: You can use the Parameters section to take in values at runtime. You can then use the values of those parameters to define how the template gets executed.

Parameters (optional)

“Values to pass to your template at runtime (when you create or update a stack). You can refer to parameters from the Resources and Outputs sections of the template”.

Option A is invalid since this is used to describes the values that are returned whenever you view your stack’s properties.
Option C is invalid since this is used to specify objects that provide additional information about the template.
Option D is invalid since this is used to specify options for the SAM Model.

<p align="center">____________________</p>

There is a new Lambda Function developed using AWS CloudFormation Templates. Which of the following attributes can be used to test the new Function with migrating 5% of traffic to the new version?
A. aws lambda create-alias –name alias name –function-name function-name \–routing-config AdditionalVersionWeights={“2″=0.05}
B. aws lambda create-alias –name alias name –function-name function-name \–routing-config AdditionalVersionWeights={“2″=5}
C. aws lambda create-alias –name alias name –function-name function-name \–routing-config AdditionalVersionWeights={“2″=0.5}
D. aws lambda create-alias –name alias name –function-name function-name \–routing-config AdditionalVersionWeights={“2″=5%}

Correct Answer: A

Explanation: Routing-Config parameter of the Lambda alias allows one to point to two different versions of the Lambda function and determine what percentage of incoming traffic is sent to each version. In the above case, a new version will be created to test the new function with 5 % of the traffic, while the original version will be used for the remaining 95% traffic.

Option B is incorrect since 5% of traffic needs to shift to a new function. The routing-config parameter should be 0.05 & not 5.
Option C is incorrect since 5% of traffic needs to shift to a new function. The routing-config parameter should be 0.05 & not 0.5.
Option D is incorrect since 5% of traffic needs to shift to a new function. The routing-config parameter should be 0.05 & not 5%.

To create an alias using the AWS Command Line Interface (AWS CLI), use the create-alias command.

`aws lambda create-alias --function-name my-function --name alias-name --function-version version-number --description "`

To change an alias to point a new version of the function, use the update-alias command.

`aws lambda update-alias --function-name my-function --name alias-name --function-version version-number`

To delete an alias, use the delete-alias command.

`aws lambda delete-alias --function-name my-function --name alias-name`

Event sources such as Amazon Simple Storage Service (Amazon S3) invoke your Lambda function. These event sources maintain a mapping that identifies the function to invoke when events occur. If you specify a Lambda function alias in the mapping configuration, you don't need to update the mapping when the function version changes.

You can point an alias to a maximum of two Lambda function versions. 

When you configure traffic weights between two function versions, there are two ways to determine the Lambda function version that has been invoked:
    - CW logs
    - For sync invocations see x-amz-executed-version header in response.

## Domain : Deployment

You are using AWS SAM to define a Lambda function and configure CodeDeploy to manage deployment patterns. With the new Lambda function working as per expectation which of the following will shift traffic from the original Lambda function to the new Lambda function in the shortest time frame?
A. Canary10Percent5Minutes
B. Linear10PercentEvery10Minutes
C. Canary10Percent15Minutes
D. Linear10PercentEvery5Minute

Correct Answer: A
Explanation: With the Canary Deployment Preference type, Traffic is shifted in two intervals. With Canary10Percent5Minutes, 10 percent of traffic is shifted in the first interval while remaining all traffic is shifted after 5 minutes.

Option B is incorrect as Linear10PercentEvery10Minutes will add 10 percent traffic linearly to a new version every 10 minutes. So, after 100 minutes all traffic will be shifted to the new version.
Option C is incorrect as Canary10Percent15Minutes will send 10 percent traffic to the new version and 15 minutes later complete deployment by sending all traffic to the new version.
Option D is incorrect as Linear10PercentEvery5Minute will add 10 percent traffic linearly to the new version every 5 minutes. So, after 50 minutes all traffic will be shifted to the new version.

<p align="center">____________________</p>

Your company has asked you to maintain an application using Elastic Beanstalk. They have mentioned that when updates are made to the application, the infrastructure maintains its full capacity. Which of the following deployment methods should you use for this requirement?
A. All at once
B. Rolling
C. Immutable
D. Rolling with additional batch

Correct Answers: C and D

Explanation: Since the only requirement is that the infrastructure should maintain its full capacity, So answers should be both C & D.

You can now use an immutable deployment policy when updating your application or environment configuration on Elastic Beanstalk. This policy is well suited for updates in production environments where you want to minimize downtime and reduce the risk from failed deployments. It ensures that the impact of a failed deployment is limited to a single instance and allows your application to serve traffic at full capacity throughout the update.

You can now also use a rolling with additional batch policy when updating your application. This policy ensures that the impact of a failed deployment is limited to a single batch of instances and allows your application to serve traffic at full capacity throughout the update.

Option A is incorrect because All at once is used to deploy the new version to all instances simultaneously. All instances in your environment are out of service for a short time while the deployment occurs.
Option B is incorrect because Rolling is used to deploy the new version in batches. Each batch is taken out of service during the deployment phase, reducing your environment’s capacity by the number of instances in a batch.

![EB All at once](../media/eb-all-at-once.png)

![EB rolling](../media/eb-rolling.png)

![EB rolling with additional batches]../media/eb-rolling-eith-additional-batches.png)

![EB immutable](../media/eb-immutable.png)

![EB blue-green](../media/eb-blue-green.png)

![EB deployment summary](../media/eb-deployment-summary.png)

<p align="center">____________________</p>

You have created an Amazon DynamoDB table with Global Secondary Index. Which of the following can be used to get the latest results quickly with the least impact on RCU (Read Capacity Unit)?
A. Query with ConsistentRead
B. Scan with ConsistentRead
C. Query with EventualRead
D. Scan with EventualRead

Correct Answer: C

Explanation: Global Secondary Index does not support Consistent read. It only supports Eventual Read. For other tables, Query with Consistent Read will provide the latest results without scanning the whole table.

Option A is incorrect as Global Secondary Index does not support Consistent read.
Option B is incorrect as Scan will impact performance as it will scan the whole table.
Option D is incorrect as Scan will impact performance as it will scan the whole table.

<p align="center">____________________</p>

Which of the following is true with respect to strongly consistent read requests from an application to a DynamoDB with a DAX cluster?
A. All requests are forwarded to DynamoDB & results are cached
B. All requests are forwarded to DynamoDB & results are stored in Item Cache before passing to application
C. All requests are forwarded to DynamoDB & results are stored in Query Cache before passing to application
D. All requests are forwarded to DynamoDB & results are not cached


Correct Answer: D
Explanation: For strongly consistent read request from an application, DAX Cluster pass all request to DynamoDB & does not cache for these requests.

Option A is incorrect as Partly correct as for consistent read request from an application, DAX Cluster pass all requests to DynamoDB & does not cache for these requests.
Option B is incorrect as Only for GetItem and BatchGetItem eventual consistent read request, Data is stored in Item Cache.
Option C is incorrect as Only for Query and Scan eventual consistent read request, Data is stored in Query Cache.

<p align="center">____________________</p>

As an API developer, you have just configured an API with the AWS API gateway service. You are testing out the API and getting the below response whenever an action is made to an undefined API resource.
{ “message”: “Missing Authentication Token” }
You want to customize the error response and make it more user-readable. How can you achieve this?
A. By setting up the appropriate method in the API gateway
B. By setting up the appropriate method integration request in the API gateway
C. By setting up the appropriate gateway response in the API gateway
D. By setting up the appropriate gateway request in the API gateway

Correct Answer: C
Explanation: This is mentioned in the AWS Documentation.

Set up Gateway Responses to Customize Error Responses

If API Gateway fails to process an incoming request, it returns the client an error response without forwarding the request to the integration backend. By default, the error response contains a short descriptive error message. For example, if you attempt to call an operation on an undefined API resource, you receive an error response with the { “message”: “Missing Authentication Token” } message. If you are new to API Gateway, you may find it difficult to understand what actually went wrong.

For some of the error responses, API Gateway allows customization by API developers to return the responses in different formats. For the Missing Authentication Token example, you can add a hint to the original response payload with the possible cause, as in this example: {“message”:”Missing Authentication Token”, “hint”:”The HTTP method or resources may not be supported.”}.

The documentation clearly mentions how this should be configured. Hence the other options are all invalid.

<p align="center">____________________</p>

Your team has currently developed an application using Docker containers. As the development lead, you now need to host this application in AWS. You also need to ensure that the AWS service has orchestration services built-in. Which of the following can be used for this purpose?
A. Consider building a Kubernetes cluster on EC2 Instances
B. Consider building a Kubernetes cluster on your on-premise infrastructure
C. Consider using the Elastic Container Service
D. Consider using the Simple Storage service to store your docker containers

Correct Answer: C
Explanation: The AWS Documentation also mentions the following.

Amazon Elastic Container Service (Amazon ECS) is a highly scalable, fast, container management service that makes it easy to run, stop, and manage Docker containers on a cluster. You can host your cluster on a serverless infrastructure that Amazon ECS manages by launching your services or tasks using the Fargate launch type. You can host your tasks on a cluster of Amazon Elastic Compute Cloud (Amazon EC2) instances that you manage by using the EC2 launch type for more control.

Options A and B are invalid since these would involve additional maintenance activities.
Option D is incorrect since this is Object-based storage.

<p align="center">____________________</p>

You are part of a development team that is in charge of creating Cloudformation templates. These templates need to be created across multiple accounts with the least amount of effort. Which of the following would assist in accomplishing this?
A. Creating Cloudformation ChangeSets
B. Creating Cloudformation StackSets
C. Make use of Nested stacks
D. Use Cloudformation artifacts

Correct Answer: B
Explanation: The AWS Documentation mentions the following.
AWS CloudFormation StackSets extends the functionality of stacks by enabling you to create, update, or delete stacks across multiple accounts and regions with a single operation. Using an administrator account, you define and manage an AWS CloudFormation template and use the template as the basis for provisioning stacks into selected target accounts across specified regions.

Option A is incorrect since this is used to make changes to the running resources in a stack.
Option C is incorrect since these are stacks created as part of other stacks.
Option D is incorrect since this is used in conjunction with Code Pipeline.

## Domain : Refactoring

A developer is writing an application that will store data in a DynamoDB table. The ratio of reads operations to write operations will be 1000 to 1, with the same data being accessed frequently.
What should the Developer enable on the DynamoDB table to optimize performance and minimize costs?
A. Amazon DynamoDB auto scaling
B. Amazon DynamoDB cross-region replication
C. Amazon DynamoDB Streams
D. Amazon DynamoDB Accelerator

Correct Answer: D
Explanation: The AWS Documentation mentions the following.

DAX is a DynamoDB-compatible caching service that enables you to benefit from fast in-memory performance for demanding applications. DAX addresses three core scenarios:

1.As an in-memory cache, DAX reduces the response times of eventually-consistent read workloads by order of magnitude, from single-digit milliseconds to microseconds.

2.DAX reduces operational and application complexity by providing a managed service that is API-compatible with Amazon DynamoDB and requires only minimal functional changes to use with an existing application.

3.For read-heavy or bursty workloads, DAX provides increased throughput and potential operational cost savings by reducing the need to over-provision read capacity units. This is especially beneficial for applications that require repeated reads for individual keys.

Option A is incorrect since this is good when you have unpredictable workloads.
Option B is incorrect since this is good for disaster recovery scenarios.
Option C is incorrect since this is good to stream data to other sources.

<p align="center">____________________</p>

How many read request units of the DynamoDB table are required for an item up to 8 KB using one strongly consistent read request?
A. 1
B. 2
C. 4
D. 8

Correct Answer: B

Explanation: One read request unit represents one strongly consistent read request, or two eventually consistent read requests for an item up to 4 KB in size.

As in the question, the item is up to 8KB, the DynamoDB table needs two read request units.

<p align="center">____________________</p>

You’ve define a DynamoDB table with a read capacity of 5 and a write capacity of 5. Which of the following statements are TRUE?
A. Strong consistent reads of a maximum of 20 KB per second
B. Eventual consistent reads of a maximum of 20 KB per second
C. Strong consistent reads of a maximum of 40 KB per second
D. Eventual  consistent reads of a maximum of 40 KB per second
E. Maximum writes of 5KB per second

Correct Answers: A, D and E
Explanation: This is also given in the AWS Documentation.

For example, suppose that you create a table with 5 read capacity units and 5 write capacity units. With these settings, your application could:

Perform strongly consistent reads of up to 20 KB per second (4 KB × 5 read capacity units).
Perform eventually consistent reads of up to 40 KB per second (twice as much read throughput).
Write up to 5 KB per second (1 KB × 5 write capacity units).
Based on the documentation, all other options are incorrect.

<p align="center">____________________</p>

You are using Amazon DynamoDB for storing all product details for an online Furniture store. Which of the following expression can be used to return the Color & Size Attribute of the table during query operations?
A. Update Expressions
B. Condition Expressions
C. Projection Expressions
D. Expression Attribute Names

Correct Answer: C
Explanation: Projection Expression is used to identify a specific attribute from a table instead of all items within a table during scan or query operation. Projection Expression can be created with Colour & Size instead of querying the full table in the above case.

Option A is incorrect as Update Expression is used to specify how an update item will modify an item’s attribute. In the above case, there is no need to modify the attributes of a table.
Option B is incorrect as Condition Expressions are used to specify a condition that should be met to modify an item’s attribute.
Option D is incorrect as Expression Attribute Names are used as an alternate name in an expression instead of an actual attribute name.

## Domain : Monitoring and Troubleshooting

Your team has just finished developing a new version of an existing application. This is a web-based application hosted on AWS. Currently, Route 53 is being used to point the company’s DNS name to the web site. Your Management has instructed you to deliver the new application to a portion of the users for testing. How can you achieve this?
A. Port the application onto Elastic beanstalk and use the Swap URL feature
B. Use Route 53 weighted Routing policies
C. Port the application onto Opswork by creating a new stack
D. Use Route 53 failover Routing policies

Correct Answer: B
Explanation: The AWS Documentation mentions the following to support this.

Weighted Routing

Weighted routing lets you associate multiple resources with a single domain name (example.com) or subdomain name (acme.example.com) and choose how much traffic is routed to each resource. This can be useful for various purposes, including load balancing and testing new versions of software.

To configure weighted routing, you create records that have the same name and type for each of your resources. You assign each record a relative weight that corresponds with how much traffic you want to send to each resource. Amazon Route 53 sends traffic to a resource based on the weight that you assign to the record as a proportion of the total weight for all records in the group:

Formula for how much traffic is routed to a given resource: 

 weight for a specified record/sum of the weights for all records.

For example, if you want to send a tiny portion of your traffic to one resource and the rest to another resource, you might specify weights of 1 and 255. The resource with a weight of 1 gets 1/256th of the traffic (1/1+255), and the other resource gets 255/256ths (255/1+255). You can gradually change the balance by changing the weights. If you want to stop sending traffic to a resource, you can change the weight for that record to 0.

Options A and C is incorrect since this would cause a full flown deployment of the new app and is just a maintenance overhead to port the application to a new service environment.
Option D is incorrect since this should only be used for failover conditions.

<p align="center">____________________</p>

Before deploying an application to production, the developer team needs to test the application latency locally using X-ray daemon. For this testing they want to skip checking Amazon EC2 instance metadata.
Which of the configuration settings can be done with daemon?
A. ~/xray-daemon$ ./xray -r
B. ~/xray-daemon$ ./xray -t
C. ~/xray-daemon$ ./xray -b
D. ~/xray-daemon$ ./xray -o

Correct Answer: D
Explanation: ~/xray-daemon$ ./xray -o command option can be used while running X-Ray daemon locally & not on Amazon EC2 instance. This will skip checking Amazon EC2 instance metadata.

Option A is incorrect as this command can be used to assume an IAM role while saving results in different accounts.
Option B is incorrect as this command can be used to bind a different TCP port for the X-Ray service.
Option C is incorrect as this command can be used to bind a different UDP port for the X-Ray service.

You can run the AWS X-Ray daemon locally on Linux, MacOS, Windows, or in a Docker container. Run the daemon to relay trace data to X-Ray when you are developing and testing your instrumented application. 

The X-Ray daemon uses the AWS SDK to upload trace data to X-Ray, and it needs AWS credentials with permission to do that. When running locally, the daemon can read credentials from an AWS SDK credentials file (.aws/credentials in your user directory) or from environment variables.

The daemon listens for UDP data on port 2000. You can change the port and other options by using a configuration file and command line options.

Run the daemon locally from the command line. Use the -o option to run in local mode, and -n to set the region (region where x-ray service is setup to listen for traces).

By default, the daemon outputs logs to STDOUT. If you run the daemon in the background, use the --log-file command line option or a configuration file to set the log file path. 

<p align="center">____________________</p>

When calling an API operation on an EC2 Instance, the following error message was returned.
A client error (UnauthorizedOperation) occurred when calling the RunInstances operation:
You are not authorized to perform this operation. Encoded authorization failure message:
oGsbAaIV7wlfj8zUqebHUANHzFbmkzILlxyj__y9xwhIHk99U_cUq1FIeZnskWDjQ1wSHStVfdCEyZILGoccGpC
iCIhORceWF9rRwFTnEcRJ3N9iTrPAE1WHveC5Z54ALPaWlEjHlLg8wCaB8d8lCKmxQuylCm0r1Bf2fHJRU
jAYopMVmga8olFmKAl9yn_Z5rI120Q9p5ZIMX28zYM4dTu1cJQUQjosgrEejfiIMYDda8l7Ooko9H6VmGJX
S62KfkRa5l7yE6hhh2bIwA6tpyCJy2LWFRTe4bafqAyoqkarhPA4mGiZyWn4gSqbO8oSIvWYPwea
KGkampa0arcFR4gBD7Ph097WYBkzX9hVjGppLMy4jpXRvjeA5o7TembBR-Jvowq6mNim0
Which of the following can be used to get a human-readable error message?
A. Use the command aws sts decode-authorization-message
B. Use the command aws get authorization-message
C. Use the IAM Policy simulator, enter the error message to get the human readable format
D. Use the command aws set authorization-message

Correct Answer: A
Explanation: This is mentioned in the AWS Documentation.

Decodes additional information about the authorization status of a request from an encoded message returned in response to an AWS request.

For example, if a user is not authorized to perform an action that he or she has requested, the request returns a Client.UnauthorizedOperation response (an HTTP 403 response). Some AWS actions additionally return an encoded message that can provide details about this authorization failure.

Because of the right command used in the documentation, all other options are incorrect.

<p align="center">____________________</p>

You are developing an application that is working with a DynamoDB table. During the development phase, you want to know how much of the Consumed capacity is being used for the queries being fired. How can this be achieved?
A. The queries by default sent via the program will return the consumed capacity as part of the result
B. Ensure to set the ReturnConsumedCapacity in the query request to TRUE
C. Ensure to set the ReturnConsumedCapacity in the query request to TOTAL
D. Use the Scan operation instead of the query operation

Correct Answer: C
Explanation: The AWS Documentation mentions the following.

By default, a Query operation does not return any data on how much read capacity it consumes. However, you can specify the ReturnConsumedCapacity parameter in a Query request to obtain this information. The following are the valid settings for ReturnConsumedCapacity.

NONE—no consumed capacity data is returned. (This is the default).
TOTAL—the response includes the aggregate number of read capacity units consumed.
INDEXES—the response shows the aggregate number of read capacity units consumed, together with the consumed capacity for each table and index that was accessed.

<p align="center">____________________</p>

Your team has started configuring CodeBuild to run builds in AWS. The source code is stored in a bucket. When the build is run, you are getting the below error.
Error: “The bucket you are attempting to access must be addressed using the specified endpoint…” When Running a Build.
Which of the following could be the cause of the error?
A. The bucket is not in the same region as the Code Build project.
B. Code should ideally be stored on EBS Volumes.
C. Versioning is enabled for the bucket.
D. MFA is enabled on the bucket.

Correct Answer: A

Explanation: This error is specified in the AWS Documentation.
Because the error is clearly mentioned, all other options are invalid.

## Domain : Security

Your company currently stores its objects in S3.  The current request rate is around 11000 GET requests per second. There is now a mandate for objects to be encrypted at rest. So you enable encryption using KMS. There are now performance issues being encountered. What could be the main reason behind this?
A. Amazon S3 will now throttle the requests since they are now being encrypted using KMS
B. You need to also enable versioning to ensure optimal performance
C. You are now exceeding the throttle limits for KMS API calls
D. You need to also enable CORS to ensure optimal performance

Correct Answer: C
Explanation: This is also mentioned in the AWS Documentation.

You can make API requests directly or by using an integrated AWS service that makes API requests to AWS KMS on your behalf. The limit applies to both kinds of requests.

Option A is incorrect because S3 will not throttle requests just because encryption is enabled.

For example, you might store data in Amazon S3 using server-side encryption with AWS KMS (SSE-KMS). Each time you upload or download an S3 object that’s encrypted with SSE-KMS, Amazon S3 makes a GenerateDataKey (for uploads) or Decrypt (for downloads) request to AWS KMS on your behalf. These requests count toward your limit, so AWS KMS throttles the requests if you exceed a combined total of 5500 (or 10,000) uploads or downloads per second of S3 objects encrypted with SSE-KMS.

Options B and D are incorrect because these will not help increase performance.

<p align="center">____________________</p>

All the objects stored in the Amazon S3 bucket need to be encrypted at rest. You are creating a bucket policy for the same.
Which header needs to be included in the bucket policy to enforce server-side encryption with SSE-S3 for a specific bucket?
A. Set “x-amz-server-side-encryption-customer-algorithm” as AES256 request header
B. Set “x-amz-server-side-encryption-bucket” as AES256 request header
C. Set “x-amz-server-side-encryption-context” as AES256 request header
D. Set “x-amz-server-side-encryption” as AES256 request header

Correct Answer: D
Explanation: To enable server-side encryption for all objects within a bucket, a request should include the “x-amz-server-side-encryption” header to request server-side encryption. A bucket policy can be created to deny all other requests. Bucket policy denies permissions to upload an object unless the request includes the x-amz-server-side-encryption header to request server-side encryption

Option A is incorrect as “x-amz-server-side-encryption-customer-algorithm” is an invalid header for encrypting objects in a bucket with SSE-S3.
Option B is incorrect as “x-amz-server-side-encryption-bucket” is an invalid header for encrypting objects in a bucket with SSE-S3
Option C is incorrect as “x-amz-server-side-encryption-context” is an invalid header for encrypting objects in a bucket with SSE-S3

<p align="center">____________________</p>

Your team is deploying a set of applications onto AWS. These applications work with multiple databases. You need to ensure that the database passwords are stored securely. Which of the following is the ideal way to store the database passwords?
A. Store them in separate Lambda functions which can be invoked via HTTPS
B. Store them as secrets in AWS Secrets Manager
C. Store them in separate DynamoDB tables
D. Store them in separate S3 buckets

Correct Answer: B
Explanation: This is mentioned in the AWS Documentation.

AWS Secrets Manager is an AWS service that makes it easier for you to manage secrets. Secrets can be database credentials, passwords, third-party API keys, and even arbitrary text. You can store and control access to these secrets centrally by using the Secrets Manager console, the Secrets Manager command-line interface (CLI), or the Secrets Manager API and SDKs.

Option A is incorrect because the Lambda function is a compute service and not used for storing credentials.
Option C is incorrect because DynamoDB is a NoSQL database service and not suitable for storing credentials.
Option D is incorrect because the S3 bucket is used to store objects and is not particularly designed to store credentials. It may have some security issues.