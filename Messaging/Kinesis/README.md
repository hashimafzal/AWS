# Kinesis

- Real-Time streaming model
- Collect, process, and analyze data in real time
- Alternative to Kafka

## Kinesis Data Streams
- Capture, process and store data streams
- Amazon Kinesis Data Streams is useful for rapidly moving data off data producers and then continuously processing the data, be it to transform the data before emitting to a data store, run real-time metrics and analytics, or derive more complex data streams for further processing. Kinesis data streams can continuously capture gigabytes of data per second from hundreds of thousands of sources such as website clickstreams, database event streams, financial transactions, social media feeds, IT logs, and location-tracking events.
- A single stream is made up of multiple shards (shards need to be predefined)
- Producers publish records to a stream.
- A record is made up of a partition key and a body (up to 1MB in size). The partition key determines to which shard the record will go to. There is ordering at the shard level.
- Publisher throughput: 1 MB/s per shard or 1000 msg/s per shard (the biggest of these two). Producers use the `PurRecord` API. Batching to reduce costs is also available.
- Consumers: Can be an app or other AWS services. They receive Partition key + body + a sequence number.
- Consumer throughput: 
    - 2 MB/s per shard shared among all consumers, with max of 5GetRecords API calls/s.
    - 2MB/s per shard per consumer (enhanced).
- Many consumers can be listening on a single shard. They consume messages in a fan-out mode. Note that if default throughput is set, they share the available throughput (2MB/s / # consumers). But if enhanced mode is enabled, you get 2MB/s for each consumer.
- Data is retained for 1 to 365 days. You have ability to replay data. 
- Immutability:" Once data is inserted it cannot be deleted.
- Capacity Modes:
    - Provisioned: You choose number of shards provisioned, scale manually or through API. Pay per shard per hour.
    - On-demand: Don't provision or manage capacity. Default capacity of 4Mb/s "in" or 4000 records per second. Scales automatically based on observed throughput peak during last 30 days. Pay per stream per hour and per in/out GB. 
- Make sure partition key is highly distributed so there is no "hot-partition" situation.
- If throughput is exceeded we get a "ProvisionedThroughputExceeded" Exception. Solutions to this: ExponentialBackoff, change partition keys to distribute more evenly or add shards.
- Shared Classic Fan out:
    - Low number of consumer applications per shard
    - Read throughput of 2MB/s per shard for all consumers of that shard
    - Max 5 GetRecords API calls/s
    - LAtency 200ms
    - Minimize Cost
    - Consumers poll data form Kinesis using GetRecords API call
    - Returns up to 10MB then throttles for 5 seconds (2MB/s) or upo to 10000 records.
- Enhanced Fan out:
    - High number of consumer applications per shard
    - Read throughput of 2MB/s per shard per consumer of that shard
    - LAtency 70ms
    - Higher Cost
    - Kinesis pushes data over HTTP2 using SubscribeToShard API
    - Soft limit of 5 consumers per shard (can be increased by creating a ticket).
- Lambdas:
    - Support for Classic and enhanced fan out consumers
    - Reads records in batches
    - You can configure batch sizes and batch windows
    - You can process up to 10 batches per shard simultaneously
Kinesis Client Library:
    - Ensures that for every shard there is a record processor running and processing that shard.
    - KCL helps you consume and process data from a Kinesis data stream by taking care of many of the complex tasks associated with distributed computing. These include load balancing across multiple consumer application instances, responding to consumer application instance failures, checkpoints processed records, and reacting to re-sharding.
    - The KCL acts as an intermediary between your record processing logic and Kinesis Data Streams.
    - Each shard is to be read by only one KCL instance
    - KCL instance communicates with DynamoDB to keep track of processed messages.
    - KCL reads from shard and checkpoints progress on DynamoDB
    - Don't confuse KCL with the actual worker that processes messages
    - Version 1 of KCL is for classic fan-out and Version 2 enhanced fan-out mode.
    - You can have more KCL apps than shards.
- Shard Splitting: To increase throughput. You separate shard1 int o shard2 and shard3. note that shard1 will be deleted once data is expired. No automatic scaling (you can create your own scaling solution though). You cant split into more that two shards in a single operation.
- Shard merging: Merge shard3 and shard4 into shard5. Old shards will be closed and deleted once data is expired, cant merge more than two shards at once.
- Amazon Kinesis Data Streams supports changes to the data record retention period of your stream. A Kinesis data stream is an ordered sequence of data records meant to be written to and read from in real time. Data records are therefore stored in shards in your stream temporarily. The time period from when a record is added to when it is no longer accessible is called the retention period. A Kinesis data stream **stores records from 24 hours by default, up to 168 hours.**

## Kinesis Firehose
- Load data into AWS data stores in a serverless fashion.
- Send records, transform them if wanted to (with lambda), and writes  data in batched to destinations (without writing code).
- Destination: S3, Redshift, ElasticSearch and any third party DBs or services. You can even use HTTP endpoint to send data to a custom destination.
- Pay for data going through Firehose
- Near Real Time
    - Data is written in batches
    - 60 seconds latency minimum or 32 MB of data at a time.
- You can send failed or all data to backup S3 bucket.

## Kinesis Data Analytics
- Analyze data streams with SQL or Apache Flink
- Takes data from sources (typically streaming sources)
- You run "streaming SQL statements" to aggregate data, make joins, calculate something, etc in real time.
- Once data is processed you output into a sink (like another stream or firehose to save the data)
- Automatic scaling
- Pay for actual consumption rate
- Create streams out of real time queries
- Use cases
    - Time series analytics.
    - Real time dashboards.
    - Real time metrics.
- Components:
    - Input:
        - The in-application stream is like a continuously updating table upon which you can perform the SELECT and INSERT SQL operations. In your application code, you can create additional in-application streams to store intermediate query results.
        - You can optionally configure a reference data source to enrich your input data stream within the application. It results in an in-application reference table.
    - App Code:
        - A series of SQL statements that process input and produce output. You can write SQL statements against in-application streams and reference tables. You can also write JOIN queries to combine data from both of these sources
        - In its simplest form, application code can be a single SQL statement that selects from a streaming input and inserts results into a streaming output. It can also be a series of SQL statements where output of one feeds into the input of the next SQL statement. Further, you can write application code to split an input stream into multiple streams. You can then apply additional queries to process these streams.
    - Outputs:
        - query results go to in-application streams. In your application code, you can create one or more in-application streams to hold intermediate results. You can then optionally configure the application output to persist data in the in-application streams that hold your application output (also referred to as in-application output streams) to external destinations.

# Notes from practice tests
- Writing data to streams
    - KPL
        - The KPL is an easy-to-use, highly configurable library that helps you write to a Kinesis data stream. It acts as an intermediary between your producer application code and the Kinesis Data Streams API actions. The KPL performs the following primary tasks:
            - Writes to one or more Kinesis data streams with an automatic and configurable retry mechanism
            - Collects records and uses PutRecords to write multiple records to multiple shards per request
            - Aggregates user records to increase payload size and improve throughput
            - Integrates seamlessly with the Kinesis Client Library (KCL) to de-aggregate batched records on the consumer
            - Submits Amazon CloudWatch metrics on your behalf to provide visibility into producer performance
        - Note that the KPL is different from the Kinesis Data Streams API that is available in the AWS SDKs. The Kinesis Data Streams API helps you manage many aspects of Kinesis Data Streams (including creating streams, resharding, and putting and getting records), while the KPL provides a layer of abstraction specifically for ingesting data.
        - Because the KPL may buffer records before sending them to Kinesis Data Streams, it does not force the caller application to block and wait for a confirmation that the record has arrived at the server before continuing execution. A call to put a record into the KPL always returns immediately and does not wait for the record to be sent or a response to be received from the server. Instead, a Future object is created that receives the result of sending the record to Kinesis Data Streams at a later time. This is the same behavior as asynchronous clients in the AWS SDK.
    - SDK APIS
    - Kinesis Agent
        - Kinesis Agent is a stand-alone Java software application that offers an easy way to collect and send data to Kinesis Data Streams. The agent continuously monitors a set of files and sends new data to your stream. The agent handles file rotation, checkpointing, and retry upon failures.
        - After installing the agent, configure it by specifying the files to monitor and the stream for the data. After the agent is configured, it durably collects data from the files and reliably sends it to the stream.
        - The agent can pre-process the records parsed from monitored files before sending them to your stream. You can enable this feature by adding the dataProcessingOptions configuration setting to your file flow. One or more processing options can be added and they will be performed in the specified order.
            - SINGLELINE: Converts a multi-line record to a single line record by removing newline characters, leading spaces, and trailing spaces.
            - CSVTOJSON: Converts a record from delimiter separated format to JSON format.
            - LOGTOJSON: Converts a record from a log format to JSON format. The supported log formats are Apache Common Log, Apache Combined Log, Apache Error Log, and RFC3164 Syslog.
- Reading data from streams
    - Lambda
    - Kinesis Data Analytics
    - Kinesis Data Firehose
    - KCL (JAVA)
        - KCL helps you consume and process data from a Kinesis data stream by taking care of many of the complex tasks associated with distributed computing. These include load balancing across multiple consumer application instances, responding to consumer application instance failures, checkpointing processed records, and reacting to resharding. The **KCL takes care of all of these subtasks so that you can focus your efforts on writing your custom record-processing logic**.
        - The KCL is different from the Kinesis Data Streams APIs that are available in the AWS SDKs. The Kinesis Data Streams APIs help you manage many aspects of Kinesis Data Streams, including creating streams, resharding, and putting and getting records. The KCL provides a layer of abstraction around all these subtasks, specifically so that you can focus on your consumer application’s custom data processing logic.
        - The KCL acts as an intermediary between your record processing logic and Kinesis Data Streams. The KCL performs the following tasks:
            - Connects to the data stream
            - Enumerates the shards within the data stream
            - Uses leases to coordinates shard associations with its workers
            -  Instantiates a record processor for every shard it manages
            - Pulls data records from the data stream
            - Pushes the records to the corresponding record processor
            - Checkpoints processed records
            - Balances shard-worker associations (leases) when the worker instance count changes or when the data stream is resharded (shards are split or merged)
        - Each KCL consumer application instance uses "workers" to process data in Kinesis shards. At any given time, each shard of data records is bound to a particular worker via a lease. For a given use case where shards are processed using EC2 instances, an EC2 instance acts as the worker for the KCL application. You can have at most one EC2 instance per shard in Kinesis for the given application. As we have 10 shards, the max number of EC2 instances is 10.
        - Typically, when you use the KCL, you should ensure that the number of instances does not exceed the number of shards (except for failure standby purposes). Each shard is processed by exactly one KCL worker and has exactly one corresponding record processor, so you never need multiple instances to process one shard. However, one worker can process any number of shards, so it's fine if the number of shards exceeds the number of instances.

- Security: Encryption
    - Automatically encrypts data before it's at rest by using an AWS KMS customer master key (CMK) you specify. Data is encrypted before it's written to the Kinesis stream storage layer, and decrypted after it’s retrieved from storage.
    - AWS KMS provides all the master keys that are used by the server-side encryption feature. AWS KMS makes it easy to use a CMK for Kinesis that is managed by AWS, a user-specified AWS KMS CMK, or a master key imported into the AWS KMS service.
    - You still must pay for the API usage costs that Amazon Kinesis Data Streams incurs on your behalf.
    - Kinesis Data Streams calls AWS KMS approximately every five minutes when it is rotating the data key. In a 30-day month, the total cost of AWS KMS API calls that are initiated by a Kinesis stream should be less than a few dollars.
    - Due to the service overhead of applying encryption, applying server-side encryption increases the typical latency of PutRecord, PutRecords, and GetRecords by less than 100μs.

- Security: VPC endpoints
    - You can use an interface VPC endpoint to keep traffic between your Amazon VPC and Kinesis Data Streams from leaving the Amazon network. Interface VPC endpoints don't require an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Interface VPC endpoints are powered by AWS PrivateLink, an AWS technology that enables private communication between AWS services using an elastic network interface with private IPs in your Amazon VPC.

- Kinesis vs SQS
![Kinesis vs SQS](../../media/kinesis-vs-sqs.jpg)

- To **scale up processing in your application**, you should test a combination of these approaches:
    - Increasing the **instance size** (because all record processors run in parallel within a process)
    - Increasing the **number of instances up to the maximum number of open shards** (because shards can be processed independently)
    - **Increasing the number of shards** (which increases the level of parallelism)

- There are two primary reasons why records may be **delivered more than one time** to your Amazon Kinesis Data Streams application: **producer retries and consumer retries.** Your application must anticipate and appropriately handle processing individual records multiple times. Applications that need strict guarantees should **embed a primary key within the record to remove duplicates later when processing**. Note that the number of duplicates due to producer retries is usually low compared to the number of duplicates due to consumer retries (make them idempotent).