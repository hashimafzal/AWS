# Secrets Manager

- Secrets Manager enables you to replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically.
- Also, you can configure Secrets Manager to automatically rotate the secret for you according to a specified schedule.
    - You define and implement rotation with an AWS Lambda function. 
    - Staging labels help you to keep track of the different versions of your secrets. Each version can have multiple staging labels attached, but each staging label can only be attached to one version.
    - Automatic secret rotation uses a Lamba function, and the Lambda function makes requests to both the database and Secrets Manager. When you turn on automatic rotation, Secrets Manager creates the Lambda function in the same VPC as your database. We recommend you create a Secrets Manager endpoint in the same VPC so that requests from the Lambda rotation function to Secrets Manager don't leave the Amazon network.
- Secrets Manager encrypts the protected text of a secret by using KMS
- Secrets Manager ensures encryption of your secret while in transit between AWS and the computers you use to retrieve the secret by using TLS.
- Security
    - You can attach AWS Identity and Access Management (IAM) permission policies to your users, groups, and roles that grant or deny access to specific secrets, and restrict management of those secrets. 
    - Alternatively, you can attach a resource-based policy directly to the secret to grant permissions specifying users who can read or modify the secret and the versions. Unlike an identity-based policy which automatically applies to the user, group, or role, a resource-based policy attached to a secret uses the Principal element to identify the target of the policy. The Principal element can include users and roles from the same account as the secret or principals from other accounts.
    - You can establish a private connection between your VPC and Secrets Manager by creating an interface VPC endpoint. Traffic between your VPC and Secrets Manager does not leave the AWS network.
- You can use the AWS managed key (aws/secretsmanager) that Secrets Manager creates to encrypt your secrets for free. If you create your own KMS keys to encrypt your secrets, AWS charges you at the current AWS KMS rate. 
- You can create secrets in a CloudFormation stack by using the AWS::SecretsManager::Secret resource in a CloudFormation template.