# DynamoDB

- **Serverless** DB managed by AWS
- **NoSQL DB** (ideal for horizontal scaling with downside of losing possibility of performing joins since in a cluster you shard data).
- You can access a **local version for development**.
- Fully Managed, Highly available with **replication across 3 AZ**
- Millions of requests per seconds, trillions of row, 100s of TB of storage
- Enables event driven programming with **DynamoDB Streams**
- Basics:   
    - **Table**: Similar to other database systems, DynamoDB stores data in tables. A table is a collection of data. They have **PARTITION KEY** (the concept of PK is different from the concept of PK for other database engines, i.e PRIMARY KEY)
    - **Items**: Each table contains zero or more items. **Max of 400kb per item**.
    - **Attributes**: Each item is composed of one or more attributes. An attribute is a fundamental data element, something that does not need to be broken down any further. Attributes in DynamoDB are similar in many ways to fields or columns in other database systems. A single attribute **may be complex in that it can nest even complexer JSON structures.** You **cannot force any attribute to NOT be NULL**, except for partition keys and sort keys (remember its NOSQL).
- Data types supported are:
    - **Scalar Types**: **String, Number, Binary, Boolean, Null**
    - **Document Types**: **List, Map** (A document type can represent a complex structure with nested attributes, such as you would find in a JSON document)
    - **Set Types**: **String Set, Number Set, Binary Set** (A set type can represent multiple scalar values). Each value within a set must be unique. The order of the values within a set is not preserved. Therefore, your applications must not rely on any particular order of elements within the set.
- **Partition Keys**
    - **PK only**: If you only use a Partition Key, you identify each element with a unique id. The selection of this partition key is important since its **used to "distribute" data**. DynamoDB uses the partition key's value as input to an internal hash function. The output from the hash function determines the partition (physical storage internal to DynamoDB) in which the item will be stored.
    - **PK + Sort Key**: Also called a composite key. DynamoDB uses the partition key value as input to an internal hash function. The output from the hash function determines the partition (physical storage internal to DynamoDB) in which the item will be stored. **All items with the same partition key value are stored together, in sorted order by sort key value**. In a table that has a partition key and a sort key, it's possible for multiple items to have the same partition key value. However, those items must have different sort key values. **A composite primary key gives you additional flexibility when querying data**. For example, if you provide only the value for Artist, DynamoDB retrieves all of the songs by that artist. To retrieve only a subset of songs by a particular artist, you can provide a value for Artist along with a range of values for SongTitle.
- In DynamoDB you need to set **read and write capacity units**:
    - **WCU: Throughput for writes (Item sizes for writes are rounded up to the next 1 KB multiple)**. Represents one write per second for an item up top 1KB in size.
        $$
        \begin{alignat*}{2}
            WCU = (ItemsToBeWrittenPerSecond)x(KBPerItem)
        \end{alignat*}
        $$

    - **RCU: Throughput for reads (Item sizes for reads are rounded up to the next 4 KB multiple)**
        - Types
            - **Eventually consistent reads**: Default type of reading. If reading is performed just after a write its possible well get unexpected response because of replication.
            - **Strongly consistent reads**: If reading is performed just after a write well get expected result. Specify you want consistent read with ConsistentRead parameter set to True in queries.
        - **1 RCU represents 1 strongly consistent read or two eventually consistent reads for an item up to 4kb in size.**
        $$
        \begin{alignat*}{2}
            RCU = (\frac{Eventually Consistent Reads}{2}) x (\frac{KBOfEachItem}{4KB})
        \end{alignat*}
        $$
        OR
        $$
        \begin{alignat*}{2}
            RCU = (Strongly Consistent Reads) x (\frac{KBOfEachItem}{4KB})
        \end{alignat*}
        $$
    - **You can setup throughput auto-scaling to meet demand**
    - Throughput can be exceeded temporarily using "burst credits" (if exceeded you will get a “ProvisionedThroughputException” and its advised to implement exponential back-off strategy).
    - RCU size rounding:
        - Item sizes for reads are rounded up to the next 4 KB multiple. For example, reading a 3,500-byte item consumes the same throughput as reading a 4 KB item. 
        - For example, if you read an item that is 3.5 KB, DynamoDB rounds the item size to 4 KB. If you read an item of 10 KB, DynamoDB rounds the item size to 12 KB.
        - A 1.5 KB item and a 6.5 KB item, DynamoDB calculates the size as 12 KB (4 KB + 8 KB), not 8 KB (1.5 KB + 6.5 KB).
        - Suppose your query returns 10 items whose combined size is 40.8 KB. DynamoDB rounds the item size for the operation to 44 KB. If a query returns 1500 items of 64 bytes each, the cumulative size is 96 KB.
- **Partitions**:
    - A partition is an **allocation of storage for a table**, backed by solid state drives (**SSDs**) and automatically **replicated across multiple Availability Zones within an AWS Region**.
    - Data is divided into partitions
    - Partition keys go through a hashing algorithm to know to what partition to go to.
    - To read an item from the table, you must specify the partition key value for the item. DynamoDB uses this value as input to its hash function, yielding the partition in which the item can be found.
    - **If the table has a composite primary key (partition key and sort key), DynamoDB calculates the hash value of the partition key in the same way as described above.** However, it stores all the items with the same partition key value physically close together, ordered by sort key value.
    - To compute the number of partitions
        $$
        \begin{alignat*}
            \# Partitions = CEILING(MAX(Capacity, Size))
        \end{alignat*}
        \newline
        Capacity = (\frac{TotalRCU}{3000}) + (\frac{TotalWCU}{1000})
        \newline
        Size = \frac{TotalSize}{10GB}
        $$
    - **WCU and RCU are spread evenly between partitions**: If you have 10 partitions and provisioned 10 RCU and WCU then you get 1 RCU and WCU per partition! Its important to **avoid hot partitions** so throughput is not exceeded.
    - DynamoDB **allocates additional partitions** to a table in the following situations
        - You **increase provisioned throughput setting it beyond what the existing partition can support**
        - If an **existing partition fills to capacity** and more storage space is required.
- **Throttling**:
    - We get burst credits but after that we are throttled and get throughput exception ("ProvisionedThroughputExceededExceptions").
    - Reasons may be:   
        - Hot Key (An item is being accessed many times)
        - Hot Partition
        - Very large items (remember that size is also a factor in capacity throughput).
    - Solutions: **Exponential back-off, Distribute partitions key, If its RCU issue you could use DAX.**
- **On-Demand provision**:
    - You can get unlimited capacity on-demand (**don't have to plan in advance**)
    - No throttling but its **more expensive** (2.5 times more expensive than provisioned capacity)
- APIs:
    - **PutItem**: **Create** a new item, **or replace** an old item with a new item
    - **UpdateItem**: **Edit** an existing item's attributes, **or adds** a new item to the table if it does not already exist
    - **GetItem**: You can specify a ProjectionExpression to just receive a subset of attributes.
    - **ConditionalWrites: Write/Update/Delete if condition is met**
    - Return Values: **Parameter to PutItem, UpdateItem and DeleteItem**. In some cases, you might want DynamoDB to **return certain attribute values as they appeared before or after you modified them**. The PutItem, UpdateItem, and DeleteItem operations have a ReturnValues parameter that you can use to return the attribute values before or after they are modified.
    - **Query**: Specify **KeyConditionExpression (Partition, sort key)** and **optionally FilterExpression** (filter after query operation before data is returned yo you). This **returns the number of items specified in "limit" or up to 1MB of data**. After that you need to **use pagination** on the results.
    - **Scan**: Read entire table, **returns up to limit or 1MB of data max**. If the total number of scanned items exceeds the maximum dataset size limit of 1 MB, the scan stops and results are returned to the user as a LastEvaluatedKey value to continue the scan in a subsequent operation (pagination). Consumes a lot of RCUs. For faster performance you can use **Parallel Scan** (scan multiple data segments at a time). Also have the option to use ProjectionExpression and FilterExpression.
        - The Scan operation can logically divide a table or secondary index into multiple segments, with multiple application workers scanning the segments in parallel. ments in parallel. Each worker can be a thread (in programming languages that support multithreading) or an operating system process. To perform a parallel scan, each worker issues its own Scan request with the following parameters:
            - Segment — A segment to be scanned by a particular worker. Each worker should use a different value for Segment.
            - TotalSegments — The total number of segments for the parallel scan. This value must be the same as the number of workers that your application will use.
        Each worker can be a thread (in programming languages that support multithreading) or an operating system process. To perform a parallel scan, each worker issues its own Scan request with the following parameters:
        ![Parallel Scan](../media/dynamodb-parallel-scan.png)
        - To make the most of your table’s provisioned throughput, you’ll want to use the Parallel Scan API operation so that your scan is distributed across your table’s partitions. But be careful that your scan doesn’t consume your table’s provisioned throughput and cause the critical parts of your application to be throttled. To avoid throttling, you need to **rate-limit your client application**.
        - Scan uses eventually consistent reads when accessing the data in a table; therefore, the result set might not include the changes to data in the table immediately before the operation began. If you need a consistent copy of the data, as of the time that the Scan begins, you can set the ConsistentRead parameter to true.
    - **DeleteItem**: Delete individual item. Support for conditional deletes.
    - **DeleteTable**
    - **BatchOperations**
        - **BatchWriteItem**
            - Up to **25 PutItem and/or DeleteItem in one call**.
            - Up to **16MB of data written** (remember max 400kb per item)
            - **No support for batch update!**
        - **BatchGetItem**
            - Return items from one or more tables
            - Up to **100 items or 16MB of data**
            - Retrieval is **done in parallel!**
        - In general, a batch operation does not fail unless all of the requests in the batch fail. For example, suppose you perform a BatchGetItemoperation but one of the individual GetItem requests in the batch fails. In this case, BatchGetItem returns the keys and data from the GetItemrequest that failed. The other GetItem requests in the batch are not affected.
    - Atomic Counters: You can use the **UpdateItem operation to implement an atomic counter, a numeric attribute that is incremented, unconditionally, without interfering with other write requests**. (All write requests are applied in the order in which they were received.) With an atomic counter, the updates are **not idempotent**. In other words, the numeric value increments each time you call UpdateItem. **An atomic counter would not be appropriate where overcounting or undercounting can't be tolerated (since it is not idempotent). In this case, it is safer to use a conditional update instead of an atomic counter.**
- **Projection Expressions** can be used in GetItem, Query or Scan.
- DynamoDB calculates the number of read capacity units consumed based on item size, not on the amount of data that is returned to an application. For this reason, the number of capacity units consumed is the same whether you request all of the attributes (the default behavior) or just some of them (using a projection expression). The number is also the same whether or not you use a filter expression. Conclusion: **FilterExpressions and ProjectionExpressions don't reduce capacity units consumed in query. Capacity units are solely based on item size**.
- **Secondary Indexes**:
    - A secondary index lets you **query the data in the table using an alternate key**, in addition to queries against the primary key.  DynamoDB doesn't require that you use indexes, but they give your applications more flexibility when querying your data.
    - **Local Secondary Index (LSI)**:
        - **Alternate Sort Key** for your table
        - **Defined at table creation** (Not modifiable once table is created.)
        - MUST be a scalar data type (string, number or binary)
        - **Up to 5 LSIs per table**
    - **Global Secondary Index (GSI)**:
        - Allows you to **define a whole new Primary Key (optionally with a sorting key)**
        - **Its like a whole new table and we need to define RCUs and WCUs for the index.**
        - **Can be added/modified after table creation**
        ![DynamoDB GSI](../media/dyanmo-gsi.png)
        - Even though it seems to be a new table, remember that if **writes are throttled on GSI, then main table will be throttled**, even if WCUs are OK in the main table! Its important to choose GSI partition key and choose WCU capacity carefully.
        - **You get a maximum of 20 GSIs per table**
        - **Strongly consistent reads** are **not supported** on global secondary indexes.
    - A **projection** is the set of **attributes that is copied from a table into a secondary index**. The partition key and sort key of the table are always projected into the index; you can project other attributes to support your application's query requirements. **When you create a secondary index, you need to specify the attributes that will be projected into the index**.
        - **KEYS_ONLY** – Each item in the index consists only of the table partition key and sort key values, plus the index key values. The KEYS_ONLY option results in the **smallest possible secondary index.**
        - **INCLUDE** – In addition to the attributes described in KEYS_ONLY, the secondary index will **include other non-key attributes** that you specify.
        - **ALL** – The **secondary index includes all of the attributes from the source table**. Because all of the table data is duplicated in the index, an ALL projection results in the **largest possible secondary index**.
- **PartiQL**:
    - **SQL syntax like language to manipulate DynamoDB**
    - Support for batch operations.
 - **Concurrency**:
    - DynamoDB is an **optimistic locking** database
        - You read a record, take note of a version number (other methods to do this involve dates, timestamps or checksums/hashes) and check that the version hasn't changed before you write the record back. (Pessimistic Locking is when you lock the record for your exclusive use until you have finished with it. It has much better integrity than optimistic locking but requires you to be careful with your application design to avoid Deadlocks. )
        - With optimistic locking, each item has an attribute that acts as a version number. If you retrieve an item from a table, the application records the version number of that item. You can update the item, but only if the version number on the server side has not changed. If there is a version mismatch, it means that someone else has modified the item before you did; the update attempt fails, because you have a stale version of the item. If this happens, you simply try again by retrieving the item and then attempting to update it. Optimistic locking prevents you from accidentally overwriting changes that were made by others; it also prevents others from accidentally overwriting your changes.
    - **Conditional updates / deletes help with concurrency issues**
    - You can ensure an item hasn't changed before altering it.
- **DAX**
    - **Cache** for DynamoDB
    - Improves read performance
    - Solves hot kwy problem: Caches hot key and your DB wont get many reads on the key.
    - All queries / reads go to cache and stay there for **5 min TTL.**
    - DAX is ideal when working with DynamoDB, use ElastiCache to store aggregated data for example.
    - **Up to 10 nodes in the cluster**
    - **Multi-AZ (3 nodes minimum recommended for production)**
- **Streams**:
    - **Ordered stream of item-level modifications**
    - **Retention up to 24 hs**
    - Changes tpo DB can en up in a stream
    - Read by EC2 or Lambdas near real time
    - You **choose the info to be sent to the stream** (4 options)
        - **KEYS_ONLY** (only the key attributes of the modified item)
        - **NEW_IMAGE** (entire item after modification)
        - **OLD_IMAGE** (entire item as before modification)
        - **NEW_AND_OLD_IMAGES** (both the new and the old images of the item)
    - **Made up of shards (you don't provision them)**
    - Item changes are **not retroactively populated** in the stream after enabling it.
    - **To integrate streams to Lambdas you need an event source mapper**.
    - AWS maintains separate endpoints for DynamoDB and DynamoDB Streams. To work with database tables and indexes, your application must access a DynamoDB endpoint. To read and process DynamoDB Streams records, your application must access a DynamoDB Streams endpoint in the same Region.
    - Stream records are organized into groups, or shards. Each shard acts as a container for multiple stream records, and contains information required for accessing and iterating through these records. The stream records within a shard are removed automatically after 24 hours.
    - Shards are ephemeral: They are created and deleted automatically, as needed. 
    - Because shards have a lineage (parent and children), an application must always process a parent shard before it processes a child shard. This helps ensure that the stream records are also processed in the correct order. (If you use the DynamoDB Streams Kinesis Adapter, this is handled for you. Your application processes the shards and stream records in the correct order. It automatically handles new or expired shards, in addition to shards that split while the application is running. For more information, see Using the DynamoDB Streams Kinesis Adapter to Process Stream Records.)
        - Amazon Kinesis Adapter is the recommended way to consume streams from Amazon DynamoDB. The DynamoDB Streams API is intentionally similar to that of Kinesis Data Streams, a service for real-time processing of streaming data at massive scale.
        -  The Kinesis Adapter implements the Kinesis Data Streams interface so that the KCL can be used for consuming and processing records from DynamoDB Streams.
- **Item TTL**:
    - Automatically delete item after expiry
    - **Does not consume WCUs!**
    - **Specified in an attribute titled TTL** (you specify a number with Unix Epoch timestamp value).
- Pagination:
    - `--page-size`: specify that AWS CLI retrieves the full list of items but with a larger number of API calls instead of one API call (**default: 1000 items**)
    - `--max-items: max`. number of items to show in the CLI (returns NextToken)
    - `--starting-token`: specify the last NextToken to retrieve the next set of items
- **Transactions**:
    - All or nothing type or operation
    - Affect many rows from many tables all at once
    - **Consumes 2x RCU and WCU** (DynamoDB performs 2 operations for every item (prepare & commit)).
    - Two operations: (**up to 25 unique items or up to 4 MB of data**)
        - **TransactGetItems** – one or more **GetItem** operations
        - **TransactWriteItems** – one or more **PutItem, UpdateItem, and DeleteItem** operations
    - Multiply above formulas by 2 to calculate RCUs and WCUs consumed for transaction operations.
    - TransactWriteItems is a synchronous and idempotent write operation that groups **up to 25 write actions in a single all-or-nothing operation**. These actions can target up to 25 distinct items in one or more DynamoDB tables within the same AWS account and in the same Region. The **aggregate size of the items in the transaction cannot exceed 4 MB (same for TransactGetItems)**.
    - With the transaction write API, you can group multiple Put, Update, Delete, and ConditionCheck actions. You can then submit the actions as a single TransactWriteItems operation that either succeeds or fails as a unit. The same is true for multiple Get actions, which you can group and submit as a single TransactGetItems operation.
    - You can **optionally include a client token when you make a TransactWriteItems call to ensure that the request is idempotent**. Making your transactions idempotent helps **prevent application errors if the same operation is submitted multiple times** due to a connection time-out or other connectivity issue. If the original TransactWriteItems call was successful, the subsequent TransactWriteItems calls with the same client token return successfully without making any changes.
    - Transactional operations provide atomicity, consistency, isolation, and durability (ACID) guarantees **only within the region where the write is made originally**. **Transactions are not supported across regions in global tables.** For example, if you have a global table with replicas in the US East (Ohio) and US West (Oregon) regions and perform a TransactWriteItems operation in the US East (N. Virginia) Region, you may observe partially completed transactions in US West (Oregon) Region as changes are replicated. Changes will only be replicated to other regions once they have been committed in the source region.
- **Write Types:**
    ![DynamoDB write types](../media//dynamo-write-types.png)
- **DynamoDB large objects pattern**: Upload large object to **s3 and store metadata in DynamoDB**. You can create all necessary metadata for querying purposes in dynamoDB. Queries are performed there instead of directly in s3 (which is not built for complex querying), and then based on results go fetch objects to s3.
- Copying data from one DynamoDb to another
    - Option1: Use AWS Data pipeline
    - Option 2: Backup and restore into new table
    - Option 3: Write code to scan and then perform PutIOtem or BatchWrites on new table.
- AWS Database migration Service can be used to migrate to DynamoDB from other databases (including relational databases).
- You can set **fine gran control on access to DynamoDB**
    - **LeadingKeys**: **limit row-level access for users on the Primary Key**
        - To implement this kind of fine-grained access control, you write an IAM permissions policy that specifies conditions for accessing security credentials and the associated permissions. You then apply the policy to IAM users, groups, or roles that you create using the IAM console. Your IAM policy can restrict access to individual items in a table, access to the attributes in those items, or both at the same time.
        - You can optionally use web identity federation to control access by users who are authenticated by Login with Amazon, Facebook, or Google.
        - You use the IAM Condition element to implement a fine-grained access control policy. By adding a Condition element to a permissions policy, you can allow or deny access to items and attributes in DynamoDB tables and indexes, based upon your particular business requirements.  
    - **Attributes**: **limit specific attributes the user can see**

## Notes from practice tests
- DynamoDB backups
    - On-Demand: 
        - Create backups when you choose.
        - You can back up and **restore your table data anytime** with a single click on the AWS Management Console or with a single API call. Backup and restore actions run with **no impact on table performance or availability**.
        - Types:
            - **DynamoDB backups**
            - **AWS Backups**:
                - Features:
                    - Scheduled backups
                    - **Cross-account and cross-Region copying**: You can automatically copy your backups to another backup vault in a different AWS Region or account, which allows you to support your data protection requirements.
                    - Cold storage tiering
    - **Point-in-time recovery**: 
        - Turn on automatic and continuous backups.
        - Point-in-time recovery helps protect your DynamoDB tables from accidental write or delete operations. With point-in-time recovery, you **don't have to worry about creating, maintaining, or scheduling on-demand backups**. For example, suppose that a test script writes accidentally to a production DynamoDB table. With point-in-time recovery, you can restore that table to **any point in time during the last 35 days**. DynamoDB maintains incremental backups of your table.
        - **Point-in-time recovery provides continuous backups until you explicitly turn it off**.
        - The point-in-time recovery process **always restores to a new table**.
        - You restore a table **without consuming any provisioned throughput** on the table
        - You can also **restore your DynamoDB table data across AWS Regions such that the restored table is created in a different Region** from where the source table resides. 
    - Both of these methods are suitable for backing up your tables for disaster recovery purposes. **However, with these methods, you can't use the data for use cases involving data analysis or extract, transform, and load (ETL) jobs.** The DynamoDB Export to S3 feature is the easiest way to create backups that you can download locally or use with another AWS service. To customize the process of creating backups, you can use use Amazon EMR, AWS Glue, or AWS Data Pipeline.
        - **DynamoDB Export to S3 feature**
            - Perform ETL against the exported data on S3 and import the data back to DynamoDB
            - Integrate the data with other services/applications
            - Build an S3 data lake from the DynamoDB data and analyze the data from various services, such as Amazon Athena, Amazon Redshift, and Amazon SageMaker.
            - This feature allows you to export data across AWS Regions and accounts without building custom applications or writing code. The exports don't affect the read capacity or the availability of your production tables.
            - This feature exports the table data in DynamoDB JSON or Amazon Ion format only.
        - **Use Amazon EMR to export your data to an S3 bucket**
        - **Use AWS Glue to copy your table to Amazon S3**
        - **Use AWS Data Pipeline** to export your table to an S3 bucket in the same account or a different account.

- **Indexes**
    - **Global secondary index** — An index with a partition key and a sort key that can be different from those on the base table. A global secondary index is considered **"global" because queries on the index can span all of the data in the base table, across all partitions.** A global secondary index is stored in its own partition space away from the base table and scales separately from the base table. **If you perform heavy write activity on the table, but a global secondary index on that table has insufficient write capacity, then the write activity on the table will be throttled.** To avoid potential throttling, the provisioned **write capacity for a global secondary index should be equal or greater than the write capacity of the base table since new updates will write to both the base table and global secondary index.**
    - Local secondary index — An index that has the same partition key as the base table, but a different sort key. A local secondary index is **"local" in the sense that every partition of a local secondary index is scoped to a base table partition that has the same partition key value.** LSI use the RCU and WCU of the main table, so you can't provision more RCU and WCU to the LSI.
    ![GSI vs LSI](../media/dynamo-gsi-vs-lsi.jpg)

- **Global Tables**
    - With global tables, you can **specify the AWS Regions where you want the table to be available.** This can significantly reduce latency for your users. So, reducing the distance between the client and the DynamoDB endpoint is an important performance fix to be considered.
    - Amazon DynamoDB global tables provide a fully managed solution for deploying a **multi-Region, multi-active database**, without having to build and maintain your own replication solution.
    - Transactional operations provide atomicity, consistency, isolation, and durability (ACID) guarantees only within the region where the write is made originally. **Transactions are not supported across regions in global tables.** For example, if you have a global table with replicas in the US East (Ohio) and US West (Oregon) regions and perform a TransactWriteItems operation in the US East (N. Virginia) Region, you may observe partially completed transactions in US West (Oregon) Region as changes are replicated. **Changes will only be replicated to other regions once they have been committed in the source region.**
    - DynamoDB global tables use a “last writer wins” reconciliation between concurrent updates. If you use Global Tables, last writer policy wins. **NO optimistic-locking**

- **You cannot attach a resource policy to a DynamoDB table**. Its does not have an  S3 bucket like policy option for security.

- An **HTTP 400 status code** indicates a problem with your request, such as **authentication failure**, **missing required parameters**, or **exceeding a table's provisioned throughput**. You have to fix the issue in your application before submitting the request again.

- In general, **Scan operations are less efficient than other operations in DynamoDB**. A Scan operation always scans the entire table or secondary index. It then filters out values to provide the result you want, essentially adding the extra step of removing data from the result set. For faster response times, design your tables and indexes so that your applications can use Query instead of Scan. For tables, you can also consider using the GetItem and BatchGetItem APIs.
![DynamoDB Scan](../media/dynamodb-scan.png)

-  Amazon DynamoDB returns data to the application in 1 MB increments, and an application performs additional Scan operations to retrieve the next 1 MB of data. Because a Scan operation reads an entire page (**by default, 1 MB**), you can **reduce the impact of the scan operation by setting a smaller page size**. The Scan operation provides a **Limit parameter** that you can use to set the page size for your request. **Each Query or Scan request that has a smaller page size uses fewer read operations and creates a "pause" between each request.** For example, suppose that each item is 4 KB and you set the page size to 40 items. A Query request would then consume only 20 eventually consistent read operations or 40 strongly consistent read operations. A larger number of smaller Query or Scan operations would **allow your other critical requests to succeed without throttling.** Even though DynamoDB distributes a large table's data across multiple physical partitions, **a Scan operation can only read one partition at a time**. For this reason, the throughput of a Scan is constrained by the maximum throughput of a single partition.

- When you create a global secondary index on a provisioned mode table, you must specify read and write capacity units for the expected workload on that index. The provisioned throughput settings of a global secondary index are **separate from those of its base table**. A Query operation on a global secondary index consumes read capacity units from the index, not the base table. **When you put, update, or delete items in a table, the global secondary indexes on that table are also updated; these index updates consume write capacity units from the index, not from the base table. To avoid potential throttling, the provisioned write capacity for a global secondary index should be equal or greater than the write capacity of the base table since new updates will write to both the base table and global secondary index.**

- To create, update, or delete an item in a DynamoDB table, use one of the following operations:
    - PutItem
    - UpdateItem
    - DeleteItem

- For each of these operations, you must specify the entire primary key, not just part of it. For example, if a table has a composite primary key (partition key and sort key), you must provide a value for the partition key and a value for the sort key. To return the number of write capacity units consumed by any of these operations, set the ReturnConsumedCapacity parameter to one of the following:
    - TOTAL — Returns the total number of write capacity units consumed.
    - INDEXES — Returns the total number of write capacity units consumed, with subtotals for the table and any secondary indexes that were affected by the operation.
    - NONE — No write capacity details are returned. (This is the default.)

- To solve hot partition problem, consider one or more of the following solutions:
    - **Increase the amount of read or write capacity** for your table to anticipate short-term spikes or bursts in read or write operations. If you decide later you don't need the additional capacity, decrease it. Take note that Before deciding on how much to increase read or write capacity, consider the best practices in designing your partition keys.
    - Implement **error retries and exponential backoff**. This technique uses progressively longer waits between retries for consecutive error responses to help improve an application's reliability. If you're using an AWS SDK, this logic is built‑in. If you're using another SDK, consider implementing it manually.
    - **Distribute your read operations and write operations as evenly as possible across your table**. A "hot" partition can degrade the overall performance of your table.
        - One way to better distribute writes across a partition key space in DynamoDB is to expand the space. You can do this in several different ways. You can add a random number to the partition key values to distribute the items among partitions (**Sharding Using Random Suffixes**), or you can use a number that is calculated based on something that you are querying on (**Sharding Using Calculated Suffixes**).
    - Implement a **caching solutio**n, such as DynamoDB Accelerator (DAX) or Amazon ElastiCache. DAX is a DynamoDB-compatible caching service that offers fast in‑memory performance for your application. If your workload is mostly read access to static data, query results can often be served more quickly from a well‑designed cache than from a database.

- RCU, WCU example: You are designing the DynamoDB table that will be used by your Node.js application. It will have to handle 10 writes per second and then 20 eventually consistent reads per second where all the items have a size of 2 KB for both operations. Which of the following are the most optimal WCU and RCU that you should provision to the table?
    - 20 RCU and 20 WCU
    - 40 RCU and 20 WCU
    - 40 RCU and 40 WCU
    - 10 RCU and 20 WCU

To get the **WCU**, you just have to follow these 3 simple steps below: 

Step #1 Get the Average Item Size by **rounding up to 1 KB**
Average Item Size = 2 KB 

Step #2 Get the WCU per Item by dividing the Average Item Size by 1 KB 
Divide the Average Item Size by 1 KB and round up the result: 
= 2 KB / 1 KB
= 2 WCU per Item **(NOT ROUNDED!)**

Step #3 Multiply the WCU per item to the number of items to be written per second 
= 2 WCU per item × 10 writes per second
= 20 WCU

To get the **RCU** with eventually consistent reads, you simply have to do the following steps:

Step #1 Get the Average Item Size by **rounding up to 4 KB**
Average Item Size = 2 KB 
= 4 KB

Step #2 Get the RCU per Item by dividing the Average Item Size by **4 KB (for strong consistency)** or **8 KB (for eventual consistency)**
Divide the Average Item Size by 8 KB since the scenario requires eventual consistency reads: 
= 4 KB / 8 KB
= 0.5 RCU per Item **(NOT ROUNDED!)**

Step #3 Multiply the RCU per item to the number of items to be written per second 
= 0.5 RCU per item × 20 writes per second
= 10 RCU

- Scan example:
    - To illustrate, let’s say that you have a table that is 50 GB in size and is provisioned with 10,000 read capacity units per second. Assume that you will perform this scan at night when normal traffic to your table consumes only 5,000 read capacity units per second. This gives you plenty of extra provisioned throughput for scanning your table, but you still don’t want it to interfere with your normal workload. If you allow your scan to consume 2,000 read capacity units, it will take about an hour to complete the scan, according to following calculation: 50 GB requires 6,553,600 read capacity units to scan, which is 50 (GB) * 1024 (MB / GB) * 1024 (KB / MB) / 2 (Scan performs eventually consistent reads, which are half the cost.) / 4 (Each 4 KB of data consumes 1 read capacity unit.) . 2,000 read capacity units per second yields 7,200,000 per hour. So 6,553,600 / 7,200,000 is equal to 0.91 hours, or about 55 minutes.
    - To make the most of your table’s provisioned throughput, you’ll want to use the Parallel Scan API operation so that your scan is distributed across your table’s partitions. But be careful that your scan doesn’t consume your table’s provisioned throughput and cause the critical parts of your application to be throttled. To avoid throttling, **you need to rate limit your client application**
    - You look for an approach to scanning a table “gently” in the background without interfering with production traffic.
