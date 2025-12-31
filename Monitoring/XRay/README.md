# XRay

- Visual analysis of our application
- Tracing solution
- XRay uses tracing techniques and then builds the visual part
- Visualize dependencies between microservices
- Review single request behaviors
- Answer questions like if we are meeting time SLA
- Understand where the current bottleneck is in.
- Tracing
    - Is the way to end to end follow a request.
    - Each component dealing with a request adds its own trace
    - Tracing is made of segments (+ subsegments)
    - Annotations can be added to traces to provide extra-information
    - You can view annotations and metadata in the segment or subsegment details in the X-Ray console.
    - You can trace every request or sample requests
    - You can drill down to traces for individual requests, or use **filter expressions** to find traces related to specific paths or users.
- How to enable it:
    - Import x ray sdk in your Java, Python, Go, NodeJs or .net app.
    - Install the X-Ray daemon (that works as a low level UDP packet interceptor). Some services already come with the daemon installed.
    - Important that app has permissions to write to XRay
- Concepts:
    - Segments: each app / service will send them. A trace segment records information about the original request, information about the work that your application does locally, and subsegments with information about downstream calls that your application makes to AWS resources, HTTP APIs, and SQL databases. A segment document can be **up to 64 kB** and contain a whole segment with subsegments, a fragment of a segment that indicates that a request is in progress, or a single subsegment that is sent separately (including metadata and annotations).
    - SubSegments: If you need more details in your segment. You can create subsegments to record calls to AWS services and resources that you make with the AWS SDK, calls to internal or external HTTP web APIs, or SQL database queries. You can also create subsegments to debug or annotate blocks of code in your application. Subsegments can contain other subsegments, so a custom subsegment that records metadata about an internal function call can contain other custom subsegments and subsegments for downstream calls. A subsegment records a downstream call from the point of view of the service that calls it. X-Ray uses subsegments to identify downstream services that don't send segments and create entries for them on the service graph. A subsegment can be embedded in a full segment document or sent independently. Send subsegments separately to asynchronously trace downstream calls for long-running requests, or to avoid exceeding the maximum segment document size.
    - Trace: Segments collected together top forma an end-to-end trace
    - Annotations: Key Value pair used to index traces and use with filters
    - Metadata: Key value pairs, not indexed, not used for searching.
    - Sampling: 
        - Don't send everything to XRay, only some requests are traced
        - By default, xray traces the first request (called reservoir) each second and then 5% (rate) of any additional requests.
        - Reservoir and Rate: If reservoir is 1 and rate is 1 then all requests will be traced
        - Changing sampling rules does not require app restart!
        - You can trace requests based on a matching criteria
- API (used by daemon)
    - PutTraceSegments: Upload segment to xray
    - PutTelemetryRecords: Upload telemetry (help with daemon metrics)
    - GetSamplingRules / GetSamplingTargets / GetSamplingStatisticsSummaries : Daemon gets what sampling rule is configured (this is why no app restart is necessary when sampling rules change)
    - Remember to set necessary policy for XRay daemon to perform these api calls to XRay service.
- API (used by users)
    - GetServiceGraph: Get trace graph
    - BatchGetTraces: Retrieves a list of traces specified by ID. Each trace is a collection of segment documents that originates from a single request.
    - GetTraceSummaries: Retrieves IDs and annotations for traces available for a specified time frame using an optional filter. 
    - GetTraceGraph: get graph but for specific trace.
- EB includes XRay by default, we need to enable it in the env configuration. (.ebextensions) and instrument it in our code. Its NOT provided for multi-container docker EB.
- ECS and XRay
    - Configuration 1: Run container of daemon on every EC2 instance. The app container must hit daemon container on a specific UDP port 2000
    - Configuration 2: Use sidecar pattern with one daemon container for every app container
    - For Fargate we necessarily need to use sidecar pattern.
    - To properly instrument your applications in Amazon ECS, you have to create a Docker image that runs the X-Ray daemon, **upload it to a Docker image repository**, and then deploy it to your Amazon ECS cluster. You can use port mappings and network mode settings in your task definition file to allow your application to communicate with the daemon container.
- You can use X-Ray to collect data across AWS Accounts. The X-Ray agent can assume a role to publish data into an account different from the one in which it is running. This enables you to publish data from various components of your application into a central account.

# Notes from practice tests
- Your company likes to operate multiple AWS accounts so that teams have their environments. Services deployed across these accounts interact with one another, and now there's a requirement to implement X-Ray traces across all your applications deployed on EC2 instances and AWS accounts. As such, you would like to have a unified account to view all the traces. What should you in your X-Ray daemon set up to make this work?
    - Configure the X-Ray daemon to use an IAM instance role
    - Create a role in the target unified account and allow roles in each sub-account to assume the role

- How should you configure the xray daemon to send trace across accounts?
    - Create a role and allow it to be assumed in your account by the outside account.

- You would like to index xray traces in order to search and filter through them efficiently, what should you use? 
    - Annotations

- AWS X-Ray works with Amazon EC2, Amazon EC2 Container Service (Amazon ECS), AWS Lambda, and AWS Elastic Beanstalk. You can use X-Ray with applications written in Java, Node.js, and .NET that are deployed on these services.

- Important env variables:
    - AWS_XRAY_TRACING_NAME: Set a service name that the SDK uses for segments. Overrides the service name that you set programmatically.
    - AWS_XRAY_SDK_ENABLED: When set to false, disables the SDK. By default, the SDK is enabled unless the environment variable is set to false.
    - AWS_XRAY_DAEMON_ADDRESS: Set the host and port of the X-Ray daemon listener. By default, the SDK uses 127.0.0.1:2000 for both trace data (UDP) and sampling (TCP).
    - AWS_XRAY_CONTEXT_MISSING: Set to LOG_ERROR to avoid throwing exceptions when your instrumented code attempts to record data when no segment is open. Valid Values:
        - RUNTIME_ERROR – Throw a runtime exception (default).
        - LOG_ERROR – Log an error and continue.
    - _X_AMZN_TRACE_ID: Contains the tracing header, which includes the sampling decision, trace ID, and parent segment ID. If Lambda receives a tracing header when your function is invoked, that header will be used to populate the _X_AMZN_TRACE_ID environment variable. If a tracing header was not received, Lambda will generate one for you.

-  The `xray-daemon.config` configuration file is primarily used in Elastic Beanstalk.

- A segment document conveys information about a segment to X-Ray. A segment document can be up to 64 kB and contain a whole segment with subsegments, a fragment of a segment that indicates that a request is in progress, or a single subsegment that is sent separately. You can send segment documents directly to X-Ray by using the PutTraceSegments API. X-Ray compiles and processes segment documents to generate queryable trace summaries and full traces that you can access by using the GetTraceSummaries and BatchGetTraces APIs, respectively. In addition to the segments and subsegments that you send to X-Ray, the service uses information in subsegments to generate inferred segments and adds them to the full trace. Inferred segments represent downstream services and resources in the service map.

- Below are the optional subsegment fields: 
    - namespace - aws for AWS SDK calls; remote for other downstream calls.
    - http - http object with information about an outgoing HTTP call.
    - aws - aws object with information about the downstream AWS resource that your application called.
    - error, throttle, fault, and cause - error fields that indicate an error occurred and that include information about the exception that caused the error.
    - annotations - annotations object with key-value pairs that you want X-Ray to index for search.
    - metadata - metadata object with any additional data that you want to store in the segment.
    - subsegments - array of subsegment objects.
    - precursor_ids - array of subsegment IDs that identifies subsegments with the same parent that completed prior to this subsegment.

- Segments and subsegments can include an annotations object containing one or more fields that X-Ray indexes for use with filter expressions. Fields can have string, number, or Boolean values (no objects or arrays). X-Ray indexes **up to 50 annotations per trace.**
    - 

- **Subsegments** provide more **granular timing information** and details about downstream calls that your application made to fulfill the original request. A subsegment can contain additional details about a call to an AWS service, an external HTTP API, or an SQL database. You can even define arbitrary subsegments to instrument specific functions or lines of code in your application.

- For services that don't send their own segments like Amazon DynamoDB, X-Ray uses subsegments to generate inferred segments and downstream nodes on the service map. This lets you see all of your downstream dependencies, even if they don't support tracing, or are external. Subsegments represent your application's view of a downstream call as a client. If the downstream service is also instrumented, the segment that it sends replaces the inferred segment generated from the upstream client's subsegment. The node on the service graph always uses information from the service's segment, if it's available, while the edge between the two nodes uses the upstream service's subsegment.