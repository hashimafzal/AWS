# CloudWatch

- Amazon CloudWatch is basically a metrics repository. An AWS service—such as Amazon EC2—puts metrics into the repository, and you retrieve statistics based on those metrics. If you put your own custom metrics into the repository, you can retrieve statistics on these metrics as well. 
- Statistics are metric data aggregations over specified periods of time. CloudWatch provides statistics based on the metric data points provided by your custom data or provided by other services in AWS to CloudWatch. Aggregations are made using the namespace, metric name, dimensions, and the data point unit of measure, within the time period you specify.
- Never deploy something without monitoring
- There are metrics for every AWS service. Metrics belong to namespaces
- Every metric can have up to 10 dimensions. A dimension is an attribute of a metric (name/value pair that is part of the identity of a metric). 
- Resolutions: 
    - Each metric is one of the following
        - Standard resolution, with data having a one-minute granularity (watch out that specifically for EC2, the default is 5 minutes)
        - High resolution, with data at a granularity of one second
    - Metrics produced by AWS services are standard resolution by default.
    - When you publish a custom metric, you can define it as either standard resolution or high resolution
    - The default for
    - When you publish a high-resolution metric, CloudWatch stores it with a resolution of 1 second, and you can read and retrieve it with a period of 1 second, 5 seconds, 10 seconds, 30 seconds, or any multiple of 60 seconds.
    - If you set an alarm on a high-resolution metric, you can specify a high-resolution alarm with a period of 10 seconds or 30 seconds, or you can set a regular alarm with a period of any multiple of 60 seconds. There is a higher charge for high-resolution alarms with a period of 10 or 30 seconds.
- If you want a more responsive ASG enable detailed monitoring! Remember that ASG works hand in hand with CW.
    - Note: EC2 Memory usage is by default not pushed to CW (it must be pushed from inside the instance as a custom metric).
- For custom metrics we use the `PutMetricData` API call to CW. Together with this you specify a resolution with `StorageResolution` parameter.
- When you publish a custom metric, you can define it as either standard resolution or high resolution. When you publish a high-resolution metric, CloudWatch stores it with a resolution of 1 second, and you can read and retrieve it with a period of 1 second, 5 seconds, 10 seconds, 30 seconds, or any multiple of 60 seconds. High-resolution metrics can give you more immediate insight into your application's sub-minute activity. But, every PutMetricData call for a custom metric is charged, so calling PutMetricData more often on a high-resolution metric can lead to higher charges.
- Important: Synchronize clocks in EC2 instance since CW accepts custom metrics coming in 2 weeks in the past and future, so logs may not be synced across instances.
- Logs:
    - Log Groups: Name usually representing an application
    - Log stream: Instances within the app / log file / containers
    - You can define log expiration policies
    - Send logs to S3, Kinesis, Lambda, ElasticSearch, etc.
    - Logs come from other AWS services (some default and all custom that we define)
    - You can set alarms based on some pattern found in logs (using filter expressions) or based on a specific output of a query defined on your logs.
    - Queries can also update a Dashboard
    - You can export logs to S3 in batches using `CreateExportTask` api call. If you need to stream logs to other services in RT you need to use Subscriptions
    - Subscriptions: Filter you apply on top of CW logs and then you specify where to send the filtered logs (destinations: Lambda, Kinesis, etc). You can use subscriptions to aggregate logs from many accounts from different regions into one S3 for example.
- CW Logs on EC2:
    - Make sure EC2s can access CW
    - Install CW Logs Agent to send logs from EC2 to CW.
    - Log Agent may even be installed on OnPremise servers.
    - Use "CW Unified Agent" (new version of the agent). You get out of the box additional metrics to CW.
    - Instance Recovery: CW integrates with EC2 to check VM and underlying hardware. If something goes wrong you enter Instance Recovery phase that moves app to new host, but maintaining Private/Public IP, Elastic IP, metadata and placement group.
- Alarms:
    - Used to trigger notifications based on any metric
    - Alarm States:
        - OK
        - INSUFFICIENT_DATA
        - ALARM
    - Period to evaluate metric: 10s, 30s or multiples of 60s.
    - Alarms can be created based on CW logs filters (maybe its better than creating a custom metric ...)
    - To test alarms and notifications you can manually set a certain alarm in ALARM state.
- Security
    - Can encrypt logs using KMS
    - At the log group level, by associating a CMK to the log group
    - You must use CW logs api (can't do this through console). You can encrypt an existing log group or specify the key at creation.
    - APIs: `associate-kms-key` and `create-log-group` (if group does not exist)
    - Remember to allow CW access to KMS through the key policy
- Events:
    - CW events is deprecated, use EventBridge instead.
    - Amazon CloudWatch Events delivers a near real-time stream of system events that describe changes in Amazon Web Services (AWS) resources. Using simple rules that you can quickly set up, you can match events and route them to one or more target functions or streams. CloudWatch Events becomes aware of operational changes as they occur.
    - You can also use CloudWatch Events to schedule automated actions that self-trigger at certain times using cron or rate expressions.


# Notes from practice tests
- CloudWatch retains metric data as follows:
    - Data points with a period of less than 60 seconds are available for 3 hours. These data points are high-resolution custom metrics.
    - Data points with a period of 60 seconds (1 minute) are available for 15 days Data points with a period of 300 seconds (5 minute) are available for 63 days.
    - Data points with a period of 3600 seconds (1 hour) are available for 455 days (15 months)

![CW Concepts](../../media/cw-concepts.jpg)

- When you create an alarm, you specify three settings to enable CloudWatch to evaluate when to change the alarm state:
    - **Period** is the length of time to evaluate the metric or expression to create each individual data point for an alarm. It is expressed in seconds. If you choose one minute as the period, there is one datapoint every minute.
    - **Evaluation Period** is the number of the most recent periods, or data points, to evaluate when determining alarm state.
    - **Datapoints to Alarm** is the number of data points within the evaluation period that must be breaching to cause the alarm to go to the ALARM state. The breaching data points do not have to be consecutive, they just must all be within the last number of data points equal to Evaluation Period.

- In the following figure, the alarm threshold is set to three units. The alarm is configured to go to the ALARM state and both Evaluation Period and Datapoints to Alarm are 3. That is, when all three datapoints in the most recent three consecutive periods are above the threshold, the alarm goes to the ALARM state. In the figure, this happens in the third through fifth time periods. At period six, the value dips below the threshold, so one of the periods being evaluated is not breaching, and the alarm state changes to OK. During the ninth time period, the threshold is breached again, but for only one period. Consequently, the alarm state remains OK.

![CW Alarms](../../media/cw-alarms.png)

- A namespace is a container for CloudWatch metrics. Metrics in different namespaces are isolated from each other, so that metrics from different applications are not mistakenly aggregated into the same statistics.  You must specify a namespace for each data point you publish to CloudWatch. You can specify a namespace name when you create a metric. These names must contain valid XML characters, and be fewer than 256 characters in length. Possible characters are: alphanumeric characters (0-9A-Za-z), period (.), hyphen (-), underscore (_), forward slash (/), hash (#), and colon (:).