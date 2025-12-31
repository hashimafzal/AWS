# S3

- Opening an object with the console generates a presigned URL: All objects and buckets are private by default. However, you can use a presigned URL to optionally share objects or allow your customers/users to upload objects to buckets without AWS security credentials or permissions. You can use presigned URLs to generate a URL that can be used to access your Amazon S3 buckets. When you create a presigned URL, you associate it with a specific action. You can share the URL, and anyone with access to it can perform the action embedded in the URL as if they were the original signing user. The URL will expire and no longer work when it reaches its expiration time.
- **Versioning is applied at the bucket level**. Versioning is a good practice. Once versioning is enabled you cant un-version it, you can only suspend it.
- Deleting a bucket with versioning enabled actually marks the object for deletion (it does not actually delete the object).
- The object with the delete marker  appears as a new object in the list. If you delete the marker then you are performing a permanent delete (you select the marker + the file to be deleted and you delete them both. Then, both marker and object will be deleted). When you get an object that has been marked for deletion, AWS responds with 404 not Found (but it still exists).
- Methods of encryption:
    - SSE-S3: Server-side encryption protects data at rest. Amazon S3 encrypts each object with a unique key.  As an additional safeguard, it encrypts the key itself with a key that it rotates regularly. When you create an object, you can specify the use of server-side encryption with Amazon S3-managed encryption keys to encrypt your data.
        - Requests that have header `'x-amz-server-side-encryption': 'AES256'` are using SSE-S3 encryption (don't mistake this with SSE-KMS alternative below).
    - SSE-KMS: Server Side encryption through KMS service. To reduce costs of calling KMS you can use "S3 Bucket Keys" for SSE-KMS. When you configure your bucket to use an S3 Bucket Key for SSE-KMS, AWS KMS generates a bucket-level key that is used to create unique data keys for new objects that you add to the bucket. This S3 Bucket Key is used for a time-limited period within Amazon S3, reducing the need for Amazon S3 to make requests to AWS KMS to complete encryption operations. This reduces traffic from S3 to AWS KMS, allowing you to access AWS KMS-encrypted objects in S3 at a fraction of the previous cost.
        - If you want to use this method you need to set a header in the request called `x-amz-server-side-encryption:aws:kms`
        - How does it work?
            - KMS can only help with 4KB of data, and S3 objects are typically larger than that.
            - It uses `GenerateDataKey` and `Decrypt` APIs (The ones used in envelope encryption).
        - S3 will need access to KMS (so you don't get access denied exception)
            - KMS key policy
            - IAM policy 
        - If you use SSE-KMS remember to enable S3 bucket key
            - Reduce calls to KMS by 99%
            - Leverage data keys and S3 bucket keys
            - The Bucket key si created from CMK
            - Bucket key is used to generate many data keys
            ![S3 Bucket Keys](../media/s3-bucket-keys.png)
    - SSE-C: server-side encryption with customer-provided encryption keys (SSE-C) allows you to set your own encryption keys. With the encryption key you provide as part of your request, Amazon S3 manages the encryption as it writes to disks and decryption when you access your objects.
        - At the time of object creation with the REST API, you can specify server-side encryption with customer-provided encryption keys (SSE-C). When you use SSE-C, you must provide encryption key information using the following request headers.
            - `x-amz-server-side​-encryption​-customer-algorithm`: Use this header to specify the encryption algorithm. The header value must be "AES256".
            - `x-amz-server-side​-encryption​-customer-key`: Use this header to provide the 256-bit, base64-encoded encryption key for Amazon S3 to use to encrypt or decrypt your data.
            - `x-amz-server-side​-encryption​-customer-key-MD5`: Use this header to provide the base64-encoded 128-bit MD5 digest of the encryption key according to RFC 1321. Amazon S3 uses this header for a message integrity check to ensure that the encryption key was transmitted without error.
        - You must use HTTPS when sending requests requiring encryption with customer provided keys (logical since keys must travel safely)
        - When you upload an object, Amazon S3 uses the encryption key you provide to apply AES-256 encryption to your data and removes the encryption key from memory. It is important to note that **Amazon S3 does not store the encryption key you provide**. Instead, it is stored in a **[randomly salted HMAC](https://www.youtube.com/watch?v=--tnZMuoK3E) value of the encryption key in order to validate future requests**. The salted HMAC value cannot be used to derive the value of the encryption key or to decrypt the contents of the encrypted object. That means, if you lose the encryption key, you lose the object.
    - Client side encryption: Client-side encryption is the act of encrypting your data locally to ensure its security as it passes to the Amazon S3 service. The Amazon S3 service receives your encrypted data; it does not play a role in encrypting or decrypting it.
        - GenerateDataKey API, generates a unique symmetric data key for client-side encryption. This operation returns a plaintext copy of the data key and a copy that is encrypted under a customer master key (CMK) that you specify. You can use the plaintext key to encrypt your data outside of AWS KMS and store the encrypted data key with the encrypted data.
        - GenerateDataKey returns a unique data key for each request. The bytes in the plaintext key are not related to the caller or the CMK.
        - To encrypt data outside of AWS KMS:
            - Use the GenerateDataKey operation to get a data key.
            - Use the plaintext data key (in the Plaintext field of the response) to encrypt your data outside of AWS KMS. Then erase the plaintext data key from memory.
            - Store the encrypted data key (in the CiphertextBlob field of the response) with the encrypted data.
        - To decrypt data outside of AWS KMS:
            - Use the Decrypt operation to decrypt the encrypted data key. The operation returns a plaintext copy of the data key.
            - Use the plaintext data key to decrypt data outside of AWS KMS, then erase the plaintext data key from memory.
- Why use KMS over S3? Basically because it gives you control over who has access to what keys and also gives you an audit trail (mas funcionalidad agregada gracias al servicio de KMS).
- In SSE-C, each key is discarded after use. Thats why customer has to provide ir on every request. Since you send the secret key, you must use in transit encryption (you must use HTTPS).
- Use s3 to serve a static website
    - Remember to disable the "block public access" option
    - Put a policy in place to GetObject for it to be accessible to anyone.
- Encryption can be set at file level or bucket level.
- Security:
    - Two types of security: User Based (IAM) and Resource based (JSON based policy) which can be Bucket policies, Object ACL or Bucket ACL. 
    - An IAM principal can access S3 object if the user IAM permissions allow it OR the resource policy allows it AND there si no explicit DENY.
    - With Bucket policy you can force objects to be encrypted at upload.
    ![S3 Force Encryption](../media/s3-security-force-encryption.png)
    - You can also specify ACLs to your bucket/objects.
    - The key point that you have to understand is that **S3 is not part of your VPC**. An EC2 instance needs to have access to the Internet, via the Internet Gateway or a NAT Instance/Gateway in order to access S3. Alternatively, you can also create a VPC endpoint so your private subnet would be able to connect to S3.
    - When to use each type of security?:
        - Object ACL: When objects are not owned by bucket owner (eg: otros suben objetos al bucket, luego deben darle accesso al owner). Remember, a bucket policy granting object permission applies only to the object owned by the bucket owner. However, the bucket owner can deny access to all the bucket and also can delete any objects inside it.
        - Bucket ACL: Grant write permissions to other service to write logs into s3.
        - Bucket Policy: Its more complete in the amount of s3 permissions you can gives. Used for cross account permissions (other AWS account or users in another account).
        - User policy: Granted by parent account to its user by attaching a policy. The resource owner can grant permissions to wither IAM user (using bucket policy).
permissions
            1. Resolve users context: Granted by parent account.
            2. Resolve bucket context: Granted by bucket owner.
            3. Resolve object context: Granted by object owner.
    - CORS:
        - Its browser based security that allows you to make requests to another server only if these other origins allow you to make these requests (using CORS headers, and preflight requests and responses).
        - If we host a website in s3, then we need to setup the correct CORS headers in case a client does a Cross-origin request to our S3 bucket.
        - Permissions override CORS settings.
        - A CORS configuration is an XML file that contains a series of rules. A configuration can have up to 100 rules. A rule is defined by one of the following tags:
            - AllowedOrigin - Specifies domain origins that you allow to make cross-domain requests.
            - AllowedMethod - Specifies a type of request you allow (GET, PUT, POST, DELETE, HEAD) in cross-domain requests.
            - AllowedHeader - Specifies the headers allowed in a preflight request.
        - Other CORS rules elements:    
            - MaxAgeSeconds  - Specifies the amount of **time in seconds (in this example, 3000) that the browser caches an Amazon S3 response to a preflight OPTIONS request** for the specified resource. By caching the response, the browser does not have to send preflight requests to Amazon S3 if the original request will be repeated.
            - ExposeHeader  - Identifies the **response headers**(in this example, x-amz-server-side-encryption, x-amz-request-id, and x-amz-id-2) **that customers are able to access from their applications** (for example, from a JavaScript XMLHttpRequest object).
    - Customers may use four mechanisms for controlling access to Amazon S3 resources: **Identity and Access Management (IAM) policies, bucket policies, Access Control Lists (ACLs), and Query String Authentication**.
    - With ACLs, customers can grant specific permissions (i.e. READ, WRITE, FULL_CONTROL) to specific users for an individual bucket or object. Amazon S3 ACLs allow users to define only the following permissions sets: READ, WRITE, READ_ACP, WRITE_ACP, and FULL_CONTROL. 
    - With Query String Authentication, customers can create a URL to an Amazon S3 object which is only valid for a limited time. Using query parameters to authenticate requests is useful when you want to express a request entirely in a URL. This method is also referred as presigning a URL.
    - Another security measure is to **force SSL transport** for requests made by clients
    ![S3 force SSL](../media/s3-security-force-ssl.png)
- S3 is strongly consistent. Read after write always works. Delete and read will always yield that the object does not exist.
- Requester Pays exists. The client incurs the costs of accessing data.
- S3 supports Batch operations: You can use S3 Batch Operations to perform large-scale batch operations on Amazon S3 objects. S3 Batch Operations can run a single operation or action on lists of Amazon S3 objects that you specify.
    - Job: contains all of the information necessary to run the specified operation on the objects listed in the manifest
    - Operations: Operation is the type of API action. Each job performs a single type of operation across all objects that are specified in the manifest
    - Task: Unit of execution for a job. A task represents a single call to an Amazon S3 or AWS Lambda API operation to perform the job's operation on a single object.
- You can log any request to S3 into another s3 bucket (has to be different or else you have an infinite loop). Logs can later be analyzed with Athena.
- Replication:
    - For replication you must have versioning enabled.
    - CRR: Cross Region Replication
    - SRR: Same Region Replication
    - Amazon S3 Replication (CRR and SRR) is configured at the S3 bucket level, a shared prefix level, or an object level using S3 object tags. 
    - After activating replication, only the new objects will be replicated, not the old ones. (you can use Batch Replication to replicate old objects to replicas). 
    - Any delete operation is not replicated/ What can be replicated are delete markers, but NOT permanent deleted. Those must be done individually for each bucket.
    - There is no "Chaining": If B1 has replication to B2 and B2 to B3. Objects created in B1 are not replicated in B3.
    - You add a replication configuration on your source bucket by **specifying a destination bucket** in the **same or different AWS region** for replication.
    - With S3 Replication (CRR and SRR), you can establish **replication rules to make copies of your objects into another storage class, in the same or a different region**. Lifecycle actions are **not replicated**, and if you want the same lifecycle configuration applied to both source and destination buckets, enable the same lifecycle configuration on both.
    - Object **tags can be replicated** across AWS Regions using Cross-Region Replication.
    - You can use replication to make copies of your objects that **retain all metadata**.
- S3 Storage classes:
    - Standard Access:
    - Standard-Infrequent Access:
    - One Zone-Infrequent Access: Only in one AZ
    - Glacier Instant Retrieval: Fast access. 90 days min storage duration
    - Glacier Flexible Retrieval: Longer retrieval times. 90 days min storage duration.
    - Glacier Deep Archive: Long hours to retrieve data. 180 days min storage duration. Lowest cost storage in the cloud. This makes it feasible to retain all the data you want for use cases like data lakes, analytics, IoT, machine learning, compliance, and media asset archiving.
    - S3 Intelligent Tiering: Move objects based on usage patterns.
- Performance:
    - Depends on prefix: You get 3500 PUTS/COPY/POST/DELETE and 5500 GET/HEAD requests per seconde per prefix in a bucket. A prefix is any path between a root folder and a file. Eg: foo/bar/file.txt, the prefix is foo/bar and we get the above performance for any operation over files in foo/bar.
    - This is important since the way you model folder structure can impact performance.
    - KMS encryption may imp[act performance since calls to KMS API are performed.
    - To optimize S3: 
        - Use **multi-part upload** (**when file is greater than 100MB**),
        - Use Transfer Acceleration through edge locations: leverages Amazon CloudFront’s globally distributed AWS Edge Locations. As data arrives at an AWS Edge Location, data is routed to your Amazon S3 bucket over an optimized network path. 
        - Use S3 Byte-range to get certain range of bytes from a single object (this parallelizes GETs by requesting specific byte ranges. Used to speed up downloads).
- S3 and Glacier Select
    - Reduce network transfer and CPU costs for client side.
    - You can query data using SQL on server side (limited to filtering rows and columns).
    - Amazon S3 Select works on objects stored in CSV, JSON, or Apache Parquet format. It also works with objects that are compressed with GZIP or BZIP2 (for CSV and JSON objects only), and server-side encrypted objects. You can specify the format of the results as either CSV or JSON, and you can determine how the records in the result are delimited.
    - For more complex querying (like aggregations) use Athena.
    ![S3 Select](../media/s3-select.jpg)
- Event notifications: React to things happening on s3. Event are published to SQS, SNS, Lambda, or EventBridge.
    - Amazon S3 event notifications are designed to be delivered at least once. Typically, event notifications are delivered in seconds but can sometimes take a minute or longer.
    - If two writes are made to a single non-versioned object at the same time, it is possible that only a single event notification will be sent. If you want to ensure that an event notification is sent for every successful write, you can enable versioning on your bucket. With versioning, every successful write will create a new version of your object and will also send event notification.
- S3 Analytics:
    - By using Amazon S3 analytics Storage Class Analysis you can analyze storage access patterns to help you decide when to transition the right data to the right storage class. You cannot use S3 Analytics to identify unintended access to your S3 resources.
- Uploading objects
    - You can upload any file type—images, backups, data, movies, etc.—into an S3 bucket. The maximum size of a file that you can upload by **using the Amazon S3 console is 160 GB**. To upload a file **larger than 160 GB, use the AWS CLI, AWS SDK, or Amazon S3 REST API**.
    - In a **single operation using the AWS SDKs, REST API, or AWS CLI**—With a single PUT operation the max size is **5GB**
    - Upload an **object in parts using the AWS SDKs, REST API, or AWS CLI**—Using the multipart upload API, you can **upload a single large object**, up to 5 TB in size. These object parts can be uploaded independently, in any order, and in parallel. You can **use a multipart upload for objects from 5 MB to 5 TB in size**.
    - To perform a multipart upload with encryption using an AWS Key Management Service (AWS KMS) customer master key (CMK), the requester must have permission to the kms:Decrypt and kms:GenerateDataKey* actions on the key. These permissions are required because Amazon S3 must decrypt and read data from the encrypted file parts before it completes the multipart upload.
    -  Each time you upload or download an S3 object that's encrypted with SSE-KMS, Amazon S3 makes a GenerateDataKey (for uploads) or Decrypt (for downloads) request to AWS KMS on your behalf. These requests count toward your quota, so AWS KMS throttles the requests if you exceed a combined total of 5,500 (or 10,000 or 30,000 depending upon your AWS Region) uploads or downloads per second of S3 objects encrypted with SSE-KMS.

- KMS encryption:
    - GenerateDataKeyWithoutPlaintext API, generates a unique symmetric data key. This operation returns a data key that is encrypted under a customer master key (CMK) that you specify.
    - GenerateDataKeyWithoutPlaintext is identical to the GenerateDataKey operation except that returns only the encrypted copy of the data key. This operation is useful for systems that need to encrypt data at some point, but not immediately. When you need to encrypt the data, you call the Decrypt operation on the encrypted copy of the key.

- Access logs with CloudTrail
    - CloudTrail **delivers access logs to the bucket owner only if the bucket owner has permissions for the same object API**.
        - Account-A owns the bucket.
        - Account-B (the requester) tries to access an object in that bucket.
        - Account-C owns the object. May be the same account as account-A.
    - CloudTrail always **delivers object-level API access logs to the requester (account-B)**. In addition, CloudTrail also **delivers the same logs to the bucket owner (account-A) only if the bucket owner owns (account-C) or has permissions for those same API actions on that object**. Otherwise, the bucket owner must get permissions, through the object's ACL to get object-level API access logs.

# Notes from practice tests
- By **default**, the AWS CLI uses a **page size of 1000** and retrieves all available items. For example, if you run aws s3api list-objects on an Amazon S3 bucket that contains 3,500 objects, the AWS CLI makes four calls to Amazon S3, handling the service-specific pagination logic for you in the background and returning all 3,500 objects in the final output. Some tokens to use in cli for pagination:
    - Server-side pagination:   
        - --no-paginate: Disabling pagination has the AWS CLI only call once for the first page of command results. For example, if you run aws s3api list-objects on an Amazon S3 bucket that contains 3,500 objects, the AWS CLI only makes the first call to Amazon S3, returning only the first 1,000 objects in the final output.
        - --max-items: Include fewer items at a time in the AWS CLI output, use the --max-items option. The AWS CLI still handles pagination with the service as described previously, but prints out only the number of items at a time that you specify. If the number of items output is fewer than the total number of items returned by the underlying API calls, the output includes a **NextToken** that you can pass to a subsequent command to retrieve the next set of items.
        - --starting-token: If the number of items output (--max-items) is fewer than the total number of items returned by the underlying API calls, the output includes a NextToken that you can pass to a subsequent command to retrieve the next set of items.
        - --page-size: specify that the AWS CLI request a smaller number of items from each call to the AWS service. The AWS CLI still retrieves the full list, but performs a larger number of service API calls in the background and retrieves a smaller number of items with each call. **This gives the individual calls a better chance of succeeding** without a timeout. Changing the **page size doesn't affect the output; it affects only the number of API calls** that need to be made to generate the output.

- Amazon S3 Transfer Acceleration
    - Bucket-level feature that enables fast, easy, and secure transfers of files over long distances between your client and an S3 bucket. Transfer Acceleration is designed to optimize transfer speeds from across the world into S3 buckets. Transfer Acceleration takes advantage of the globally distributed edge locations in Amazon CloudFront. As the data arrives at an edge location, the data is routed to Amazon S3 over an optimized network path.

- Consistency model:
    - Amazon S3 delivers strong read-after-write consistency automatically for all applications, without changes to performance or availability, without sacrificing regional isolation for applications, and at no additional cost. With strong consistency, S3 simplifies the migration of on-premises analytics workloads by removing the need to make changes to applications, and reduces costs by removing the need for extra infrastructure to provide strong consistency. After a successful write of a new object, or an overwrite or delete of an existing object, any subsequent read request immediately receives the latest version of the object. S3 also provides strong consistency for list operations, so after a write, you can immediately perform a listing of the objects in a bucket with any changes reflected.
    - Here are examples of this behavior for **objects in a bucket** (**strongly consistent model**):
        - A process writes a new object to Amazon S3 and immediately lists keys within its bucket. The new object appears in the list.
        - A process replaces an existing object and immediately tries to read it. Amazon S3 returns the new data.
        - A process deletes an existing object and immediately tries to read it. Amazon S3 does not return any data because the object has been deleted.
        - A process deletes an existing object and immediately lists keys within its bucket. The object does not appear in the listing.
        - Write and read an the same time (R1 might return color = ruby or color = garnet)
        ![Concurrent Write and Read](../media/s3-concurrent-write-and-read.png)
        - Concurrent Writes: W2 begins before W1 has received an acknowledgement. Therefore, these writes are considered concurrent. Amazon S3 internally uses last-writer-wins semantics to determine which write takes precedence. However, the order in which Amazon S3 receives the requests and the order in which applications receive acknowledgements cannot be predicted because of various factors, such as network latency. For example, W2 might be initiated by an Amazon EC2 instance in the same Region, while W1 might be initiated by a host that is farther away. The best way to determine the final value is to perform a read after both writes have been acknowledged.
        ![Concurrent Writes](../media/s3-concurrent-writes.png)
    - **Bucket configurations have an eventual consistency model**:
        - f you delete a bucket and immediately list all buckets, the deleted bucket might still appear in the list.
        - If you enable versioning on a bucket for the first time, it might take a short amount of time for the change to be fully propagated. We recommend that you wait for 15 minutes after enabling versioning before issuing write operations (PUT or DELETE requests) on objects in the bucket.
- Amazon S3 supports **bucket policies** that you can use if you **require server-side encryption** for all objects that are stored in your bucket. For example, you can set a bucket policy that denies permission to upload an object (s3:PutObject) to everyone if the request does not include the `x-amz-server-side-encryption` header requesting server-side encryption with SSE-KMS. When you upload an object, **you can specify the KMS key** using the `x-amz-server-side-encryption-aws-kms-key-id` header which you can use to require a specific KMS key for object encryption. **If the header is not present in the request, Amazon S3 assumes the default KMS key.** Regardless, the KMS key ID that Amazon S3 uses for object encryption must match the KMS key ID in the policy, otherwise Amazon S3 denies the request.
- Using the `put-bucket-policy --policy` command you apply a policy at the bucket level, not on objects. You can use S3 Access Control Lists (ACLs) instead to manage permissions of S3 objects.

- This is unlikely to happen as there is no direct way to restrict a user from uploading a file with a specific size constraint.

- To enable the **cross-region replication** feature in S3, the **following items should be met**:
    - The source and destination buckets must have **versioning enabled**.
    - The source and destination buckets must be in different AWS Regions.
    - Amazon **S3 must have permissions to replicate objects** from that source bucket to the destination bucket on your behalf.

- Amazon **S3 Object Lock** is enabled in the bucket is incorrect because this feature simply enables you to store objects using a **write-once-read-many (WORM) model**. You can use it to **prevent an object from being deleted or overwritten** for a fixed amount of time or indefinitely, but it will not affect your cross-region replication configuration.

- **AWS Transfer for SFTP**: A fully managed service that enables the transfer of files directly into and out of Amazon S3 using the **Secure File Transfer Protocol (SFTP) which is also known as Secure Shell (SSH) File Transfer Protocol.** It does not provide a fast, easy, and secure way to transfer files over long distances between your client and your Amazon S3 bucket.