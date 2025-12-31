# [IAM ABAC (Attribute-based access control)](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html#tutorial_abac_step3)

- Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes.
- In AWS, these attributes are called tags. You can attach tags to IAM resources, including IAM entities (users or roles) and to AWS resources.
- You can define policies that use tag condition keys to grant permissions to your principals based on their tags.
- These ABAC policies can be designed to allow operations when the principal's tag matches the resource tag.
- In IAM, you implement RBAC (role-based access) by creating different policies for different job functions. You then attach the policies to identities (IAM users, groups of users, or IAM roles).
- No all services support authorization with tags. You need to look them up before implementing ABAC.
- You can configure your SAML-based or web identity provider to pass session tags to AWS. When your employees federate into AWS, their attributes are applied to their resulting principal in AWS.
- Employees sign in with IAM user credentials and then assume the IAM role for their team and project. The same policy is attached to all of the roles. Actions are allowed or denied based on tags. Employees can create new resources, but only if they attach the same tags to the resource that are applied to their role. This ensures that employees can view the resource after they create it. Administrators are no longer required to update policies with the ARN of new resources. IAM administrators can add a new role for new projects. They can create and tag a new IAM user to allow access to the appropriate role. Administrators are not required to edit a policy to support a new project or team member.

## Steps:

- Create Users
    - Each IAM users needs permissions to assume roles with the same tags.
    - The following policy allows a user to assume any role in your account with the access- name prefix. The role must also be tagged with the same project, team, and cost center tags as the user.
    ```json
    {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "TutorialAssumeRole",
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            // allows a user to assume any role in your account (the root account) with the access- name prefix.
            "Resource": "arn:aws:iam::123456789012:role/access-*",
            "Condition": {
                // The condition is that the users have the necessary tags to do so. For more info look at conditions in https://docs.aws.amazon.com/IAM/latest/UserGuide/list_identityandaccessmanagement.html. The resource is another account (i.e PrincipalTag). Use this key (iam:ResourceTag/tag-key) to compare the tag key-value pair that you specify in the policy with the key-value pair attached to the resource
                "StringEquals": {
                    "iam:ResourceTag/access-project": "${aws:PrincipalTag/access-project}",
                    "iam:ResourceTag/access-team": "${aws:PrincipalTag/access-team}",
                    "iam:ResourceTag/cost-center": "${aws:PrincipalTag/cost-center}"
                }
            }
        }
    ]
    }
    ```
    - The above policy uses policy variables inside the conditions block. When you use a policy variable, AWS substitutes a value from the request context key in place of the variable in your policy. https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html
    - To scale this tutorial to a large number of users, you can attach the policy to a group and add each user to the group.
    - To each user we attach the above policy
- Create ABAC Policy
    - This policy will be added to a role created later in the tutorial.
    - The following policy allows principals to create, read, edit, and delete resources, but only when those resources are tagged with the same key-value pairs as the principal.
    - When a principal creates a resource, they must add access-project, access-team, and cost-center tags with values that match the principal's tags.
```json
    {
 "Version": "2012-10-17",
 "Statement": [
     {
         "Sid": "AllActionsSecretsManagerSameProjectSameTeam",
         "Effect": "Allow",
         "Action": "secretsmanager:*", // policy grows as Secrets Manager grows. If Secrets Manager adds a new API operation, you are not required to add that action to the statement.
         "Resource": "*",
         "Condition": {
             "StringEquals": { // returns true if the specified tag keys are present on the resource, and their values match the principal's tags. This block returns false for mismatched tags, or for actions that don't support resource tagging
                 "aws:ResourceTag/access-project": "${aws:PrincipalTag/access-project}",
                 "aws:ResourceTag/access-team": "${aws:PrincipalTag/access-team}",
                 "aws:ResourceTag/cost-center": "${aws:PrincipalTag/cost-center}"
             },
             "ForAllValues:StringEquals": { // returns true if every tag key passed in the request is included in the specified list. This is done using ForAllValues with the StringEquals condition operator. If the requester includes a tag key that is not in the list, the condition returns false.
                 "aws:TagKeys": [
                     "access-project",
                     "access-team",
                     "cost-center",
                     "Name",
                     "OwnedBy"
                 ]
             },
             "StringEqualsIfExists": { // returns true if the request supports passing tags, if all three of the tags are present, and if they match the principal tag values. This block also returns true if the request does not support passing tags. This is thanks to ...IfExists in the condition operator. The block returns false if there is no tag passed during an action that supports it, or if the tag keys and values don't match.
                 "aws:RequestTag/access-project": "${aws:PrincipalTag/access-project}",
                 "aws:RequestTag/access-team": "${aws:PrincipalTag/access-team}",
                 "aws:RequestTag/cost-center": "${aws:PrincipalTag/cost-center}"
             }
         }
     },
     {
         "Sid": "AllResourcesSecretsManagerNoTags",
         "Effect": "Allow",
         "Action": [
             "secretsmanager:GetRandomPassword",
             "secretsmanager:ListSecrets"
         ],
         "Resource": "*"
     },
     {
         // allows read-only operations if the principal is tagged with the same access-team tag as the resource. This is allowed regardless of the project or cost-center tag.
         "Sid": "ReadSecretsManagerSameTeam",
         "Effect": "Allow",
         "Action": [
             "secretsmanager:Describe*",
             "secretsmanager:Get*",
             "secretsmanager:List*"
         ],
         "Resource": "*",
         "Condition": {
             "StringEquals": {
                 "aws:ResourceTag/access-team": "${aws:PrincipalTag/access-team}"
             }
         }
     },
     {
         // denies requests to remove tags with keys that begin with "access-" from Secrets Manager. These tags are used to control access to resources, therefore removing tags might remove permissions.
         "Sid": "DenyUntagSecretsManagerReservedTags",
         "Effect": "Deny",
         "Action": "secretsmanager:UntagResource",
         "Resource": "*",
         "Condition": {
             "ForAnyValue:StringLike": {
                 "aws:TagKeys": "access-*"
             }
         }
     },
     {
         // denies access to create, edit, or delete Secrets Manager resource-based policies. These policies could be used to change the permissions of the secret.
         "Sid": "DenyPermissionsManagement",
         "Effect": "Deny",
         "Action": "secretsmanager:*Policy",
         "Resource": "*"
     }
 ]
}
```
- Create roles
    - We are now going to create roles and attach the above policy to each and every one of them. Each role has its corresponding tag. We will have one role per job function
        - Project Pegasus Engineering
        - Project Pegasus Quality Assurance
        - Project Unicorn Engineering
        - Project Unicorn Quality Assurance
- Test creating secrets
    - The permissions policy attached to the roles allows the employees to create secrets. This is allowed only if the secret is tagged with their project, team, and cost center.
    - To test you sign in as one of the created users and assume the one of the roles created above. If the corresponding tags match, it will successfully assume the role. 
