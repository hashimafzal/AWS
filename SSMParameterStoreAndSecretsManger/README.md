# SSM Parameter Store

- Secure storage for configuration and secrets (**plain text or secrets** with KSM)
- Optional Seamless Encryption using KMS (you not only need permissions for SSM but also for KMS)
- Serverless, scalable, durable, easy SDK
- Version tracking of configurations / secrets
- Configuration management using path & IAM
- Notifications with CloudWatch Events
- Integration with CloudFormation
- Use hierarchies to store configurations and secrets (folder like structure)
- Option of Standard offering vs Advanced offering
![SSM offerings](../media/ssm-offerings.png)
- Advanced offering supports parameter policies which allow you to
    - Set TTL on parameters
    - Notifications on actions taken on parameters
- Also known as AWS Systems Manager Parameter Store: Provides secure, hierarchical storage for configuration data management and secrets management. You can store data such as passwords, database strings, Amazon Machine Image (AMI) IDs, and license codes as parameter values. You can store values as plain text or encrypted data. You can reference Systems Manager parameters in your scripts, commands, SSM documents, and configuration and automation workflows by using the unique name that you specified when you created the parameter.
- Parameter Store offers the following benefits and features:
    - Use a secure, scalable, hosted secrets management service (No servers to manage).
    - Improve your security posture by separating your data from your code.
    - Store configuration data and secure strings in hierarchies and track versions.
    - Control and audit access at granular levels.
    - Configure change notifications and trigger automated actions.
    - Tag parameters individually, and then secure access from different levels, including operational, parameter, Amazon EC2 tag, or path levels.

- Reference AWS Secrets Manager secrets by using Parameter Store parameters.

# Secrets Manger
- New version of SSM
- **Only store secrets!** Feature of rotating secrets (using a lambda function that actually performs the needed rotation)
- Feature of integrating with RDS for automatic secret rotation (no need for implementing lambda function here, AWS provides the function implementation)
- Leverages KMS
- 