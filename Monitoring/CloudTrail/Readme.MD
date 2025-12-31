# CloudTrail

- Enabled by default
- Get history of events / API calls made within your AWS account that came from
    - SDK
    - CLI
    - Console
    - IAM Users and IAM roles
- Integrate with CW logs or S3 to save history
- In general they are management events (operations that are performed on resources in your AWS account).
- You may see scenario-based questions asking you to select one of CloudWatch vs CloudTrail vs Config. Just remember this thumb rule -
    - Think resource performance monitoring, events, and alerts; think CloudWatch.
    - Think account-specific activity and audit; think CloudTrail.
    - Think resource-specific history, audit, and compliance; think Config.
- You cannot use CloudTrail to debug and trace data across accounts.
- By default, CloudTrail event log files are encrypted using Amazon S3 server-side encryption (SSE).