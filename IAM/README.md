# IAM

- Its recommended to never use root user. Just create it to create users from it and grant permissions.
- A policy in AWS is an object in AWS, that when associated with an identity or resource, defines their permissions.
- IAM is **global service**.
- IAM Federation: Used for enterprise customers. It integrates with the companies own repos of users such as Active Directory. (you sign into AWS through company credentials).
- The concept is that you **create policies that you later attach to identities**. You also have the ability to **attach inline policies** to users directly.
- **Principal: An entity in AWS that can perform actions and access resources**. A principal can be an:
    - **AWS account root user**
    - **An IAM user**
    - **A role.** 
- **IAM Users**:
    - An AWS Identity and Access Management (IAM) user is an entity that you create in AWS to **represent the person or application** that uses it to interact with AWS. A user in AWS consists of a **name and credentials.**
- **IAM User Groups**:
    - An IAM user group is a collection of IAM users. User groups let you specify permissions for multiple users, which can make it  easier to manage the permissions for those users. An IAM user group is a collection of IAM users. User groups let you specify permissions for multiple users, which can make it easier to manage the permissions for those users.
- **IAM Roles**:
    - An **IAM role** is an IAM identity that you can create in your account that has specific permissions. An IAM role is **similar to an IAM user**, in that it is an AWS identity with permission policies that determine what the identity can and cannot do in AWS. **However, instead of being uniquely associated with one person, a role is intended to be assumable by anyone who needs it.** Also, a role does not have standard long-term credentials such as a password or access keys associated with it. Instead, **when you assume a role, it provides you with temporary security credentials for your role session**. You can use roles to delegate access to users, applications, or services that don't normally have access to your AWS resources.
    - **AWS service role**: A **role that a service assumes** to perform actions in your account on your behalf. When you set up some AWS service environments, you must define a role for the service to assume. This service role must include all the permissions required for the service to access the AWS resources that it needs. 
    - **AWS service role for EC2**: A special type of **service role that an application running on an Amazon EC2 instance can assume** to perform actions in your account. This role is assigned to the EC2 instance when it is launched. Applications running on that instance can retrieve temporary security credentials and perform actions that the role allows.
    - **AWS service-linked role**: A unique type of **service role that is linked directly to an AWS service**. Service-linked roles are predefined by the service and include all the permissions that the service requires to call other AWS services on your behalf.
    - **Role Chaining**: Role chaining is when you **use a role to assume a second role through the AWS CLI or API**. For example, RoleA has permission to assume RoleB. You can enable User1 to assume RoleA by using their long-term user credentials in the AssumeRole API operation. This returns RoleA short-term credentials. With role chaining, you can use RoleA's short-term credentials to enable User1 to assume RoleB. Role chaining limits your AWS CLI or AWS API role session to a **maximum of one hour**. **When you use the AssumeRole API operation to assume a role, you can specify the duration of your role session with the DurationSeconds parameter**.
    - **Delegation**: The granting of **permissions to someone to allow access to resources that you control**. **Delegation involves setting up a trust between two accounts**. The first is the account that owns the resource (the trusting account). The second is the account that contains the users that need to access the resource (the trusted account). To delegate permissions you create a IAM role that has two policies: 
        - **Permission policy**: Grants the user of the role the permissions needed
        - **Trust Policy**: **Which trusted account members are allowed to assume the role**. Define the principals that you trust to assume the role. A user who assumes a role temporarily gives up his or her own permissions and instead takes on the permissions of the role. When the user exits, or stops using the role, the original user permissions are restored. Trust policies define which principal entities (accounts, users, roles, and federated users) can assume the role. **An IAM role is both an identity and a resource that supports resource-based policies**. For this reason, you must attach both a trust policy and an identity-based policy to an IAM role. The IAM service supports only one type of resource-based policy called a role trust policy, which is attached to an IAM role.
    - **Federation**: The creation of a **trust relationship between an external identity provider and AWS**. Users using Federation are assigned to an IAM role. The user also receives temporary credentials that allow the user to access your AWS resources.
- IAM policy structure:
![IAM Policy Structure](../media/iam-policy-structure.png)
- To protect users and groups:
    - Setup a **password policy**: Select what password must include, setup password rotations, allow users to change passwords (you can also prevent password reuse).
    - You can also require **MFA** (**Virtual** MFA device like google/authy, or a **U2F**, **Fob MFA** device por AWS GovCloud which are physical versions for MFA).
- Accessing AWS:
    - Through console with user + password + MFA.
    - Through CLI or SDK using "access key id" (like username) and "secret access key" (like password).
- To use CLI you need to configure aws client using "**aws configure**" command. This creates two files in .aws directory: **config and credentials files**.
- CLI command errors sometimes come in an eligible form. To get additional information you can use the STS command line tool by passing the "**decode-authorization-message**" option. Note: user must have necessary permissions to do so. If you are calling the command from an ec2 instance it must have a IAM role attached to it to access STS.
 ```bash
aws sts decode-authorization-message --encoded-message <value>
```
- You can **change between AWS accounts on a single CLI instance** by using `--profile` option. Use `aws config --profile <profile-name>`
to configure a new profile. To execute commands with specific profile run `aws <command> --profile <profile-name>`.
- **You can also use MFA with CLI and SDKs**. It works by getting temporary credentials (temporary "access key id" and "secret access key") to use aws resources.
    - Inside cmd, run `aws sts get-session-token --serial-number <your-users-arn> --token-code <MFA-code>`.
    - After using STS GetSessionToken API call (which asks you for your MFA token), you setup a new profile and use those credentials all in the same CLI
    - Then add the generated token into .aws/credentials file (under a new entry called `aws_session_token`)
    - Once that is done, any time you do API call using this profile its going to use these temporary credentials.
- **Fun fact ... the cli uses python SDK (boto3).**
- SDK calls without specifying **region defaults to us-east-1**.
- Tools: 
    - For policy generation you can use **IAM console Visual Editor** or the **AWS Policy Generator**.
    - **AWS Policy Simulator**: Tool to **test your policies**. Very useful to see where in the JSON policy you have deny/allow access to resources and certain API calls on a particular service. Another way to test them is to **use "--dry-run"** option on certain commands from cli. [See video](https://www.youtube.com/watch?v=1IIhVcXhvcE). Is a sandbox environment, it does not actually change the policies. You then need to copy the desired policy and apply it through IAM console.
    - IAM has a **credentials Report** which lists all your account's users and the status of their various credentials.
    - IAM has **Access Advisor** which helps see permissions granted to a particular user and when those services where last accessed. To help identify the **unused roles**, IAM reports the last-used timestamp that represents when a role was last used to make an AWS request. Your security team can use this information to identify, analyze, and then confidently remove unused roles. This helps improve the security posture of your AWS environments. This does not provide information about non-IAM entities such as S3, hence it's not a correct choice here.
    - **IAM Access Analyzer**: AWS IAM Access Analyzer helps you identify the resources in your organization and accounts, such as Amazon S3 buckets or IAM roles, that are shared with an **external entity**. This lets you identify unintended access to your resources and data, which is a security risk. You can set the scope for the analyzer to an organization or an AWS account. This is your zone of trust. The analyzer scans all of the supported resources within your zone of trust. When Access Analyzer finds a policy that allows access to a resource from outside of your zone of trust, it generates an active finding.
- **To get the IAM role a specific EC2 instance has you can use the EC2 metadata**. You access it by curling "http:<IP>/latest/metadata" URL. You get the **IAM Role name but not the role specifics**.
- When you call AWS HTTP API (through skd or cli basically), you sign the request using access keys. If you are using SDK or CLI all requests are signed for you. If you are not planning to use SDK or CLI you need to sign them yourself. to do that you need to use **"Signature v4 signing"** (sigv4). **Authentication information can travel inside the headers of requests or through query string in the URL.**
- **Explicit "Denys" override "Allows"**. This is important when IAM policies conflict with a policy specified at the resource level, like a specific s3 bucket.
- **Dynamic Policy Generation**: Used when you don't know the exact value of a resource or condition when you write a policy. You generalize the policy using **policy variables** that come from the request context (request context is info associated to each request done to AWS, like user data, the operation wanted to be performed and the resource upon the operation is intended to).
- The **cli uses credentials and configurations located in multiple places**. [See this article](https://aws.amazon.com/es/premiumsupport/knowledge-center/iam-ec2-user-role-credentials/). Some take precedence over others:
    - **Command line options**
    - **Env variables**
    - CLI **credentials file** (setup with `aws configure`).
    - **Container credentials** (ECS): Temporary credentials given to containers based on the role associated to each task.
    - **CLI configuration file**
    - **Container credentials**
    - **Instance profile credentials** (instance roles): 
        - Temporary credentials for the role given to an EC2 instance. The credentials are delivered to the instance through the metadata service.
        - The instance profile contains the role and can provide the role's temporary credentials to an application that runs on the instance. Those temporary credentials can then be used in the application's API calls to access resources and to limit access to only those resources that the role specifies. Note that only one role can be assigned to an EC2 instance at a time, and all applications on the instance share the same role and permissions.
        - Imagine that you have an IAM user for working in the development environment and you occasionally need to work with the production environment at the command line with the AWS CLI. You already have an access key credential set available to you. This can be the access key pair that is assigned to your standard IAM user. Or, if you signed in as a federated user, it can be the access key pair for the role that was initially assigned to you. If your current permissions grant you the ability to assume a specific IAM role, then you can identify that role in a "profile" in the AWS CLI configuration files. That command is then run with the permissions of the specified IAM role, not the original identity.
        - Note that when you specify that profile in an AWS CLI command, you are using the new role. In this situation, you cannot make use of your original permissions in the development account at the same time. The reason is that only one set of permissions can be in effect at a time.
- Providing access to an IAM user in another AWS account that you own
    ![IAM cross account](../media/iam-cross-account.png)
    1. In the production account, an administrator uses IAM to **create the UpdateApp role** in that account. In the role, the administrator defines a **trust policy** that specifies the development account as a Principal, meaning that authorized users from the development account can use the UpdateApp role. The administrator also defines a **permissions policy** for the role that specifies the read and write permissions to the Amazon S3 bucket named productionapp.
    2. An administrator grants members of the Developers group **permission to switch to the role**. This is done by granting the Developers group permission to call the AWS Security Token Service (AWS STS) **AssumeRole API** for the UpdateApp role. Any IAM user that belongs to the Developers group in the development account can now switch to the UpdateApp role in the production account.
    3. The user requests switches to the role
    4. AWS STS returns temporary credentials
    5. The temporary credentials allow access to the AWS resource
- IAM Authorization Model:
![IAM Auth Model](../media/iam-auth-model.png)
- Managed Policy vs Customer managed Policy vs Inline
    - **AWS MAnaged Policy**
        - Maintained by AWS
        - Good for power users and admins
        - Updated in case AWS services change
    - **AWS Customer Managed Policy**
        - Best practice, reusable, can be applied to many principals
        - Version controlled + rollback, central change management
    - **Inline**
        - Strict one to one relationship between policy and principal
        - Policy is deleted if you delete the IAM principal
- **To give a service a role you need to be able to pass a role**. Make sure principal can perform `iam:PassRole`. It often comes with `iam:GetRole` to view the role being passed. Can a role be passed to any service? NO. **Roles can only be passed to what their trust policy allows**. A trust policy for the role that allows the service to assume the role.
    - The PassRole permission helps you make sure that a user doesn’t pass a role to an EC2 instance where the role has more permissions than you want the user to have. For example, Alice might be allowed to perform only EC2 and S3 actions. If Alice could pass a role to the EC2 instance that allows additional actions, she could log into the instance, get temporary security credentials via the role she passed, and make calls to AWS that you don’t intend.
    - Remember that every role has permissions and trust relationships (trust policy)


## Notes from practice tests
- When you create an IAM user, you can choose to allow console or programmatic access. If console access is allowed, the IAM user can sign in to the console using a user name and password. Or if programmatic access is allowed, the user can use access keys to work with the CLI or API.

-  An IAM role is both an identity and a resource that supports resource-based policies. For that reason, you must attach both a trust policy and an identity-based policy to an IAM role. Trust policies define which principal entities (accounts, users, roles, and federated users) can assume the role. 

- [Types of policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
    - **identity-based policies**
        - Identity-based policies are JSON permissions policy documents that control what actions an **identity** (users, groups of users, and roles) can perform, on which resources, and under what conditions.
        - Can be Managed policies, Customer Manged policies or inline policies
    - **Resource-based policies**
        - Resource-based policies are JSON policy documents that you **attach to a resource** such as an Amazon S3 bucket. These policies grant the specified principal permission to perform specific actions on that resource and defines under what conditions this applies.
        - **Resource-based policies are inline policies.**
        - There are no managed resource-based policies.
        - Adding a cross-account principal to a resource-based policy is only half of establishing the trust relationship. When the principal and the resource are in separate AWS accounts, you must also use an identity-based policy to grant the principal access to the resource. 
    - **permissions boundaries**
        - Advanced feature for using a **managed policy to set the maximum permissions that an identity-based policy can grant to an IAM entity.** An entity's permissions boundary allows it to perform only the actions that are allowed by both its identity-based policies and its permissions boundaries
    - **Organizations SCPs**
        - Service for grouping and **centrally managing the AWS accounts that your business owns**. If you enable all features in an organization, then you can apply service control policies (SCPs) to any or all of your accounts. **SCPs are JSON policies that specify the maximum permissions for an organization or organizational unit (OU)**. The SCP limits permissions for entities in member accounts, including each AWS account root user. 
    - **ACLs**
        - Access control lists (ACLs) are service policies that allow you to control which principals in another account can access a resource.
        - **ACLs are similar to resource-based policies, although they are the only policy type that does not use the JSON policy document format.**
        - **Amazon S3, AWS WAF, and Amazon VPC** are examples of services that support ACLs. 
    - **Session policies**
        - Advanced policies that you pass as a parameter when you programmatically create a temporary session for a role or federated user. The permissions for a session are the intersection of the identity-based policies for the IAM entity (user or role) used to create the session and the session policies.
        - The resulting session's permissions are the intersection of the session policies and the resource-based policies plus the intersection of the session policies and identity-based policies.
    
- **Policy structure**
    - Version
    - Statement: Use this main policy element as a container for the following elements. You can include more than one statement in a policy.
        - **Sid**: optional statement ID to differentiate between your statements.
        - **Effect**: Use Allow or Deny to indicate whether the policy allows or denies access.
        - **Principal (required only in some cases)**: If you create a resource-based policy, you must indicate the account, user, role, or federated user to which you would like to allow or deny access. If you are creating an IAM permissions policy to attach to a user or role, you cannot include this element. **The principal is implied as that user or role.**
        - **Action**: Include a list of actions that the policy allows or denies.
        - **Resource (Required in only some circumstances)**: If you create an IAM permissions policy, you must specify a list of resources to which the actions apply. If you create a resource-based policy, this element is optional. **If you do not include this element, then the resource to which the action applies is the resource to which the policy is attached.**
        - **Condition (Optional):** Specify the circumstances under which the policy grants permission.

- [Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)
    - **Trusted Advisor** draws upon **best practices learned** from serving hundreds of thousands of AWS customers. Trusted Advisor inspects your AWS environment, and then **makes recommendations** when opportunities exist to save money, improve system availability and performance, or help close security gaps.

- [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html)
    - Amazon Inspector is a **vulnerability management service** that continuously scans your AWS workloads for vulnerabilities. Amazon Inspector automatically discovers and scans Amazon EC2 instances and container images residing in Amazon Elastic Container Registry (Amazon ECR) for software vulnerabilities and unintended network exposure.
    - When a software vulnerability or network issue is discovered, Amazon Inspector creates a finding. A finding describes the vulnerability, identifies the affected resource, rates the severity of the vulnerability, and provides remediation guidance. Details of a finding for your account can be analyzed in multiple ways using the Amazon Inspector console, or you can view and process your findings through other AWS services.

- **For some AWS services**, you can grant **cross-account access** to your resources. To do this, you **attach a policy directly to the resource that you want to share, instead of using a role as a proxy**. The **resource that you want to share must support resource-based policies**. Unlike an identity-based policy, a resource-based policy specifies who (which principal) can access that resource. IAM roles and resource-based policies delegate access across accounts **only within a single partition**. For example, assume that you have an account in US West (N. California) in the standard aws partition. You also have an account in China (Beijing) in the aws-cn partition. You can't use an Amazon S3 resource-based policy in your account in China (Beijing) to allow access for users in your standard aws account. Cross-account access with a resource-based policy has some advantages over cross-account access with a role. With a resource that is accessed through a resource-based policy, the **principal still works in the trusted account and does not have to give up his or her permissions to receive the role permissions**. In other words, the principal continues to have access to resources in the trusted account at the same time as he or she has access to the resource in the trusting account. Some of the AWS services that support resource-based policies: 
    - Amazon **S3 buckets** 
    - Amazon Simple Notification Service (**Amazon SNS**) topics 
    - Amazon Simple Queue Service (**Amazon SQS**) queues

- **The maximum level of access that an account can delegate to sub accounts is the access level that is granted to the account.** Eg: a resource-based policy granted full access to an S3 bucket in AccountA to AccountB. AccountB root user will be able to delegate to a sub-account, eg: User2 a subset of the permissions granted to the account (or all of them), eg: Give User2 read-only access to bucket in AccountA.

- Bucket owner granting permissions to objects it does not own
    - **By default, only the resource owner can access these resources.**
    - The AWS account that uploads objects owns those objects. The bucket owner does not have permissions on the objects that other accounts own\
    - **By default, when another AWS account uploads an object to your S3 bucket, that account (the object writer) owns the object, has access to it, and can grant other users access to it through ACLs.** You can use **Object Ownership** to change this default behavior so that ACLs are disabled and you, as the bucket owner, automatically own every object in your bucket. As a result, access control for your data is based on policies, such as IAM policies, S3 bucket policies, virtual private cloud (VPC) endpoint policies, and AWS Organizations service control policies (SCPs).
    - Example:
    ![Bucket and object ownership example](../media/s3-object-and-bucket%20ownership-example.png)
        1. Account A administrator user attaches a bucket policy with two statements.
            - Allow cross-account permission to Account B to upload objects.
            - Allow a user in its own account to access objects in the bucket.
        2. Account B administrator user uploads objects to the bucket owned by Account A.
        3. Account B administrator updates the object ACL adding grant that gives the bucket owner full-control permission on the object.
        4. User in Account A verifies by accessing objects in the bucket, regardless of who owns them.

-  **AWS Organizations**
    - Its an account management service that enables you to **consolidate multiple AWS accounts into an organization that you create and centrally manage.** AWS Organizations includes account management and consolidated billing capabilities that enable you to better meet the budgetary, security, and compliance needs of your business. As an administrator of an organization, you can create accounts in your organization and **invite existing accounts to join the organization**. You can group your accounts into organizational units (OUs) and attach different access policies to each OU.As an administrator of the management account of an organization, you can use service control policies (**SCPs**) to specify the maximum permissions for member accounts in the organization. In SCPs, you can restrict which AWS services, resources, and individual API actions the users and roles in each member account can access. This block remains in effect even if an administrator of a member account explicitly grants such permissions in an IAM policy. AWS Organizations expands that control to the account level by giving you control over what users and roles in an account or a group of accounts can do. In other words, the user can access only what is allowed by both the AWS Organizations policies and IAM policies. If either blocks an operation, the user can't access that operation.
    - The **consolidated billing feature in AWS Organizations** allows you to consolidate payment for multiple AWS accounts or multiple AISPL accounts. Each organization in AWS Organizations has a master account that pays the charges for all the member accounts. If you have access to the master account, you can see a combined view of the AWS charges that are incurred by the member accounts. You also can get a cost report for each member account.
    - Policy Types:
        - Authorization policies:
            - Service control policies (SCPs) offer central control over the maximum available permissions for all of the accounts in your organization.
        - Management policies: Management policies enable you to centrally configure and manage AWS services and their features.
            - AI services opt-out policy (control data collection for AWS AI services for all of your organization's accounts)
            - Backup policy (entrally manage and apply backup plans to the AWS resources)
            - Tag policy (standardize the tags attached to the AWS resources )
![AWS Organizations Policy Types](../media/iam-organizations.png)



- **Good practice to use temporary credentials when possible!**

- Imagine that you have Amazon EC2 instances that are critical to your organization. Instead of directly granting your users permission to terminate the instances, you can create a role with those privileges. Then allow administrators to switch to the role when they need to terminate an instance. Doing this adds the following layers of protection to the instances:
    - You must explicitly grant your users permission to assume the role.
    - Your users must actively switch to the role using the AWS Management Console or assume the role using the AWS CLI or AWS API.
    - You can add multi-factor authentication (MFA) protection to the role so that only users who sign in with an MFA device can assume the role.

- A role specifies a set of permissions that you can use to access AWS resources. In that sense, it is similar to an IAM User. A principal (person or application) assumes a role to receive temporary permissions to carry out required tasks and interact with AWS resources. The role can be in your own account or any other AWS account. To assume a role, an application calls the AWS STS AssumeRole API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. This session has the same permissions as the identity-based policies for that role. **GetSessionToken and AssumeRole work hand in hand**

- Another best practice they recommend is to **delete root user access keys**. You use an access key (an access key ID and secret access key) to make programmatic requests to AWS. However, the access key for your AWS account root user gives full access to all your resources for all AWS services, including your billing information. You cannot reduce the permissions associated with your AWS account root user access key. This is a common security concern that should be handled appropriately.

- It is **not recommended** to provide **all users console and programmatic access.**

- Your sign-in page URL has the following format, by default: `https://Your_AWS_Account_ID.signin.aws.amazon.com/console/`. If you create an AWS account alias for your AWS account ID, your sign-in page URL looks like the following example: `https://Your_Alias.signin.aws.amazon.com/console/`

- **If your identity store is not compatible with SAML 2.0**, then you can build a **custom identity broker** application to perform a similar function. The broker application authenticates users, requests temporary credentials for users from AWS (STS), and then provides them to the user to access AWS resources. The application verifies that employees are signed into the existing corporate network's identity and authentication system, which might use LDAP, Active Directory, or another system. The identity broker application then obtains temporary security credentials for the employees. To get temporary security credentials, the identity broker application calls either AssumeRole or GetFederationToken to obtain temporary security credentials, depending on how you want to manage the policies for users and when the temporary credentials should expire. The call returns temporary security credentials consisting of an AWS access key ID, a secret access key, and a session token. The identity broker application makes these temporary security credentials available to the internal company application. The app can then use the temporary credentials to make calls to AWS directly. The app caches the credentials until they expire, and then requests a new set of temporary credentials.
![IAM Custom Broker](../media/iam-custom-broker.png)