# Practice Test 12

[Link to practice test](https://www.udemy.com/course/aws-certified-developer-associate-practice-exams-amazon/learn/quiz/5097194/result/744023524#content)

- Score 80%
![PT 12 Results](../media/pt-12-results.png)

# ToDo list review:
- Security
- Refactoring
- Deployment
- Monitor and Troubleshooting
- Review Development with AWS services


## Review Security
- Some static assets stored in an S3 bucket need to be accessed by a user on the development account. The S3 bucket is in the production account. According to the company policy, the sharing of full credentials between accounts is prohibited. What steps should be done to delegate access across the two accounts? (Select THREE.)
    - Log in to the production account and create a policy that will use STS to assume the IAM role in the development account. Attach the policy to the IAM users
    - On the production account, create an IAM role and specify the development account as a trusted entity.
    -Set the policy that will grant access to S3 for the IAM role created in the development account
    - Set the policy that will grant access to S3 for the IAM role created in the production account
    - On the development account, create an IAM role and specify the production account as a trusted entity
    - Log in to the development account and create a policy that will use STS to assume the IAM role in the production account. Attach the policy to corresponding IAM users.

https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html

https://aws.amazon.com/blogs/security/how-to-enable-cross-account-access-to-the-aws-management-console/

https://tutorialsdojo.com/aws-identity-and-access-management-iam/

<p align="center">____________________</p>

- A developer has an application that stores sensitive data to an Amazon DynamoDB table. AWS KMS must be used to encrypt the data before sending it to the table and to manage the encryption keys. Which of the following features are supported when using AWS KMS? (Select TWO.)
    - Import your own key material to an asymmetric CMK
    - Re-enabling disabled keys
    - Automatic key rotation for CMKs in custom key stores
    - Use AWS Certificate Manager as a custom key store
    - Creation of symmetric and asymmetric keys

https://docs.aws.amazon.com/kms/latest/developerguide/overview.html

https://aws.amazon.com/kms/faqs/

https://tutorialsdojo.com/aws-key-management-service-aws-kms/

<p align="center">____________________</p>

- A developer needs to view the percentage of used memory and the number of TCP connections of instances inside an Auto Scaling Group. To achieve this, the developer must send the metrics to Amazon CloudWatch. Which approach provides the MOST secure way of authenticating a CloudWatch PUT request?
    - Create an IAM role with cloudwatch:PutMetricData permission for the new Auto Scaling launch configuration from which you launch instances.
    - Create an IAM user with programmatic access. Attach a cloudwatch:PutMetricData permission and store the access key and secret key in the instance's configuration file
    - Create an IAM user with programmatic access. Attach a cloudwatch:PutMetricData permission and update the Auto Scaling launch configuration to insert the access key and secret key into the instance via user data
    - Modify the existing Auto Scaling launch configuration to use an IAM role with the cloudwatch:PutMetricData permission for the instances

https://docs.aws.amazon.com/autoscaling/ec2/userguide/change-launch-config.html

https://docs.aws.amazon.com/autoscaling/ec2/userguide/LaunchConfiguration.html

https://tutorialsdojo.com/amazon-cloudwatch/

<p align="center">____________________</p>

- A team of developers needs permission to launch EC2 instances with an instance role that will allow them to update items in a DynamoDB table. Each developer has access to IAM users that belongs in the same IAM group. Which of the following steps must be done to implement the solution?
    - Create an IAM role with an IAM policy that will allow access to the DynamoDB table. Add the EC2 service to the trust policy of the role. Create a custom policy with iam:GetRolePolicy and iam:PutRolePolicy permissions. Attach the policy to the IAM group
    - Create an IAM role with an IAM policy that will allow access to the DynamoDB table. Add the EC2 service to the trust policy of the role. Create a custom policy with iam:PassRole permission. Attach the policy to the IAM group.
    - Create an IAM role with an IAM policy that will allow access to the EC2 instances. Add the DynamoDB service to the trust policy of the role. Create a custom policy with iam:GetRole permission. Attach the policy to the IAM group
    - Create an IAM role with an IAM policy that will allow access to the EC2 instances. Add the DynamoDB service to the trust policy of the role. Create a custom policy with iam:PassRole permission. Attach the policy to the IAM group

https://aws.amazon.com/blogs/security/granting-permission-to-launch-ec2-instances-with-iam-roles-passrole-permission/

https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html

https://tutorialsdojo.com/aws-identity-and-access-management-iam/

## Review Refactoring
- A developer wants to cut down the execution time of the scan operation to a DynamoDB table during periods of low demand without interfering with typical workloads. The operation consumes half of the strongly consistent read capacity units within regular operating hours. How can the developer improve this scan operation?
    - Use eventually consistent reads for the scan operation instead of strongly consistent reads
    - Use a parallel scan operation 
    - Perform a rate-limited sequential scan operation 
    - Perform a rate-limited parallel scan operation.

https://aws.amazon.com/blogs/developer/rate-limited-scans-in-amazon-dynamodb/

https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Scan.html

https://amazon-dynamodb-labs.com/design-patterns/ex2scan/step2.html

https://tutorialsdojo.com/amazon-dynamodb/

## Review Deployment

## Review Monitor and Troubleshooting
- A company wants to know how its monolithic application will perform on a microservice architecture. The Lead Developer has deployed the application on Amazon ECS using the EC2 launch type. He terminated the container instance after testing; however, the container instance still appears as a resource in the ECS cluster. What is the possible cause of this?
    - When a container instance is terminated in the stopped state, the container instance is not automatically deregistered from the cluster.
    - When a container instance is terminated in the running state, the container instance is not automatically deregistered from the cluster
    - After terminating the container instance in the running state, the container instance must be manually deregistered in the Amazon ECS Console
    - After terminating the container instance in the stopped state, the container instance must be manually deregistered in the Amazon EC2 Console since it was launched using the the EC2 launch type

https://aws.amazon.com/premiumsupport/knowledge-center/deregister-ecs-instance/

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_instances.html

https://tutorialsdojo.com/amazon-elastic-container-service-amazon-ecs/

<p align="center">____________________</p>

- A development team is building a website that displays an analytics dashboard. The team uses AWS CodeBuild to compile the website from a source code residing on Github. A member was instructed to configure CodeBuild to run with a proxy server for privacy and security reasons. A RequestError timeout error appears on CloudWatch whenever CodeBuild is accessed. Which is a possible solution to resolve the issue?
    - Modify the proxy element of the buildspec.yml file on the source code root directory.
    - Modify the artifacts element of the buildspec.yml file on the source code root directory
    - Modify the phases element of the AppSpec.yml file on the source code root directory
    - Modify the proxy element of the AppSpec.yml file on the source code root directory.

https://docs.aws.amazon.com/codebuild/latest/userguide/troubleshooting.html

https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec.proxy

https://tutorialsdojo.com/aws-codebuild/

https://www.youtube.com/watch?v=1zA6mK9BdA4

## Review Development with AWS services
- A developer is building a serverless NodeJs application consisting of an API Gateway and AWS Lambda. The developer wants to log certain events tagged with a unique identifier of the Lambda functions’ invocation request. Which approach should the developer take?
    - Get the awsRequestId from the context object and log it to a file.
    - Get the awsRequestId from the context object and log it to the console
    - Get the awsRequestId from the event object and log it to the console.
    - Get the awsRequestId from the event object and log it to a file.

https://docs.aws.amazon.com/lambda/latest/dg/nodejs-context.html

https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html

https://tutorialsdojo.com/aws-lambda/

<p align="center">____________________</p>

- An application is hosted in the us-east-1 region. The app needs to be recreated on the us-east-2, ap-northeast-1, and ap-southeast-1 region using the same Amazon Machine Image (AMI). As the developer, you have to use AWS CloudFormation to rebuild the application using a template. Which of the following actions is the most suitable way to configure the CloudFormation template for the scenario?
    - Copy the AMI of the instance from the us-east-1 region to the us-east-2, ap-northeast-1, and ap-southeast-1 region. Then, add a Mappings section wherein you will define the different Image Id for the three regions. Use the region name as the key in mapping to its correct Image Id. Lastly, use the Fn::FindInMap function to retrieve the desired Image Id from the region key.
    - Copy the AMI of the instance from the us-east-1 region to the us-east-2, ap-northeast-1, and ap-southeast-1 region. Then, add a Mappings section wherein you will define the different Image Id for the three regions. Use the region name as the key in mapping to its correct Image Id. Lastly, use the Fn::ImportValue function to retrieve the desired Image Id from the region key
    - Copy the AMI of the instance from the us-east-1 region to the us-east-2, ap-northeast-1, and ap-southeast-1 region. Then, add a Mappings section wherein you will define the different Image Id for the three regions. Use the region name as the key in mapping to its correct Image Id. Lastly, use the Fn::GetAtt function to retrieve the desired Image Id from the region key
    - Copy the AMI of the instance from the us-east-1 region to the us-east-2, ap-northeast-1, and ap-southeast-1 region. Then, add a Parameters section wherein you will define the different Image Id for the three regions. Use the region name as the key in mapping to its correct Image Id. Lastly, use the Ref function to retrieve the desired Image Id from the region key

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/mappings-section-structure.html

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-findinmap.html

https://tutorialsdojo.com/aws-cloudformation/

<p align="center">____________________</p>

- A developer wants to expose a legacy web service that uses an XML-based Simple Object Access Protocol (SOAP) interface through API Gateway. However, there is a compatibility issue since most modern applications communicate data in JSON format. Which is the most cost-effective method that will overcome this issue?
    - Use API Gateway to create a RESTful API. Transform the incoming JSON into XML using mapping templates. Forward the request into the SOAP interface by using a Lambda function and parse the response (XML) into JSON before sending back to API Gateway.
    - Use API Gateway to create a WebSocket API. Transform the incoming JSON into XML using mapping templates. Forward the request into the SOAP interface by using a Lambda function and parse the response (XML) into JSON before sending back to API Gateway
    - Use API Gateway to create a RESTful API. Transform the incoming JSON into XML for the SOAP interface through an Application Load Balancer and vice versa. Put the legacy web service behind the ALB
    - Use API Gateway to create a RESTful API. Send the incoming JSON to an HTTP server hosted on an EC2 instance and have it transform the data into XML and vice versa before sending it to the legacy application

https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html

https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-data-transformations.html

https://github.com/mwittenbols/How-to-use-Lambda-and-API-Gateway-to-consume-XML-instead-of-JSON

https://tutorialsdojo.com/amazon-api-gateway/

<p align="center">____________________</p>

- A company is planning to launch an online cross-platform game that expects millions of users. The developer wants to use an in-house authentication system for user identification. Each user identifier must be kept consistent across devices and platforms. How can the developer achieve this?
    - Use developer-authenticated identities in Amazon Cognito to generate unique identifiers for the users.
    - Generate a universally unique identifier (UUID) for each device. Store the UUID with the user in a DynamoDB table
    - Generate a unique IAM access key for each user and use the access key ID as the unique identifier
    - Create an IAM Role for each user and use its Amazon Resource Name (ARN) as unique identifiers

https://docs.aws.amazon.com/cognito/latest/developerguide/developer-authenticated-identities.html

https://aws.amazon.com/blogs/mobile/understanding-amazon-cognito-authentication-part-2-developer-authenticated-identities/

https://aws.amazon.com/blogs/mobile/amazon-cognito-announcing-developer-authenticated-identities/

https://tutorialsdojo.com/amazon-cognito/

<p align="center">____________________</p>

- A developer is building a ReactJS application that will be hosted on Amazon S3. Amazon Cognito handles the registration and signing of users using the AWS Software Development Kit (SDK) for JavaScript. The JSON Web Token (JWT) received upon authentication will be stored on the browser's local storage. After signing in, the application will use the JWT as an authorizer to access an API Gateway endpoint. What are the steps needed to implement the scenario above? (Select THREE.)
    - Create an Amazon Cognito User Pool.
    - Create an Amazon Cognito Identity Pool
    - On the API Gateway Console, create an authorizer using the Cognito User Pool ID.
    - Choose and set the authentication provider for your website
    - Set the name of the header that will be used from the request to the Cognito User Pool as a token source for authorization.
    - Set the name of the header that will be used from the request to the Cognito Identity Pool as a token source for authorization

https://aws.amazon.com/premiumsupport/knowledge-center/cognito-user-pools-identity-pools/

https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html

https://tutorialsdojo.com/amazon-cognito/

https://tutorialsdojo.com/amazon-cognito-user-pools-and-identity-pools-explained/

<p align="center">____________________</p>

- A startup plans to use Amazon Cognito User Pools to easily manage their users' sign-up and sign-in workflows to an application. To save time from designing the User Interface (UI) for the login page, the development team has decided to use Cognito's built-in UI. However, the product manager finds the UI bland and instructed the developer to include the product logo on the web page. How should the developer meet the above requirements?
    - Upload the logo to the Amazon Cognito app settings and use that logo on the custom login page.
    - Upload the logo to an S3 bucket and point the S3 endpoint on the custom login page
    - Create a login page with the product logo and upload it to Amazon Cognito
    - Create a login page with the product logo and upload it to an S3 bucket. Point the S3 endpoint in the Cognito app settings

https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-app-ui-customization.html

https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html

https://tutorialsdojo.com/amazon-cognito/

<p align="center">____________________</p>

- A developer is building an application that uses Amazon CloudFront to distribute thousands of images stored in an S3 bucket. The developer needs a fast and cost-efficient solution that will allow him to update the images immediately without waiting for the object’s expiration date. Which solution meets the requirements?
    - Update the images by using versioned file names.
    - Update the images by invalidating them from the edge caches
    - Disable the CloudFront distribution and re-enable it to update the images in all edge locations
    - Upload the new images in the S3 bucket and wait for the objects in the edge locations to expire to reflect the changes

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/UpdatingExistingObjects.html

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html

https://aws.amazon.com/blogs/aws/simplified-multiple-object-invalidation-for-amazon-cloudfront/

https://tutorialsdojo.com/amazon-cloudfront/