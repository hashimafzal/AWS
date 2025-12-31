# CloudFront

- CloudFront is a CDN (**Content Delivery network**)
- **CF with S3**:
    - Used for **distributing files** and **caching** them at the edge.
    - Can be used as an ingress top upload files to S3.
    - With **CF Origin Access Identity** security feature you allow your S3 bucket to only allow communication from cloudfront and nowhere else (OAI is an IAM role for your s3 bucket for secure integration to CF). Note that if this approach is used, your **s3 files can be private since the only ones accessing them will be the edge locations**.
    - Could also work nicely with s3 bucket website.
    - Have in mind that DNS might take a few hours to distribute the content to edge locations. So you might not be able to access resources directly through Edge location URL right away. See [this link](https://stackoverflow.com/questions/38735306/aws-cloudfront-redirecting-to-s3-bucket) for more info.
- CF and HTTP origins:
    - Not only support fo s3 but for **any origin (typically other AWS resources) with HTTP support.**
    - In case origins are EC2s or ELBs, the SGs wrapping them must allow access from CF edge locations (list of public IPs for Edge locations is in the web).
- **Geo-restriction**: Restrict who can access your distribution through a **whitelist or a blacklist**.
- Cloudfront with s3 vs S3 Cross Region Replication:
    -  Cloudfront with s3 is great for **static content** that must be **available everywhere**.
    - S3 Cross Region Replication: Great for **dynamic content** that needs to be available at **low-latency in few regions**.
- Caching on CF
    - Cache for **TTL**, **resolve requests locally** or **request origin** for info. The idea is to maximize cache hits and minimize origin requests.
    - Good practice to separate static and dynamic distributions
    - If you have a long TTL and you update a file thats already cached on CF, the changes wont be reflected immediately in CF. To solve this we can use **invalidation**. You **flush edge location caches** based on the invalidation.
    - The **origin servers add headers to requests indicating how much you want the request to stat in the cache** in th edge location (**default is 24hr**).
- **Signed URL or Signed Cookies**: Use when you want to distribute paid content through CF.
    - **Signed url** gives access to **individual files** (one signed url per file)
    - **Signed cookies** give access to **multiple files at once** (one signed cookie for many files).
    - It works the following way: 
        - Client asks app to give it a signed url for a resource (authentication and authorization is solely done at app level).
        - If permitted, app returns a signed url to client
        - Client can then ask for CF for a certain file
        - **CF will use OAI to access file in S3 bucket and return it to client**.
- **Don't mistake CF signed URL with S3 Presigned URL!**
- Pricing:
    - Depends on the mount of data out per edge location.
    - You have an option to reduce costs by reducing number of edge locations
        - Price Class All: All regions and best performance.
        - Price Class 200: Most regions, but excludes the most expensive regions.
        - Price Class 100: Only least expensive regions.
- **Multiple origins**: I want to send **traffic to different origins based on content type or url path pattern**.
- **Origin groups**: Consists of **one primary and one secondary origin**. If the primary fails, the second one is used.
    - By leveraging this you can have S3 in different regions for high availability
        - Setup two S3 buckets with replication
        - If one region fails it goes to the second region.
    - CloudFront **routes all incoming requests to the primary origin, even when a previous request failed over to the secondary origin**. CloudFront only sends requests to the secondary origin after a request to the primary origin fails.
    - CloudFront **fails over to the secondary origin only when the HTTP method of the viewer request is GET, HEAD, or OPTIONS. CloudFront does not failover when the viewer sends a different HTTP method (for example POST, PUT, and so on).**
    - Setting up **two origins are enough** to set up an origin failover.
    - **Failover occurs when**:
        - The primary origin returns an HTTP status code that you’ve **configured for failover**
        - CloudFront **fails to connect** to the primary origin
        - The response from the primary origin takes too long (**times out**)
- **Field level encryption**:
    - Used to **protect user sensitive** data through the application stack
    - Adds **additional security to HTTPS**
    - Uses **asymmetric encryption to encrypt data at the edge location close to the user**
    - You can ask edge locations to encrypt **specific HTTP request fields before sending data to origin.**
    - Origins use their private keys to access info.
- **Lambda@edge**:
    - Extension for AWS lambda
    - Lets you **execute function that customizes the content that cloudfront delivers.**
    - You associate a distribution with a Lambda@edge function. **CF intercepts the request and responses at edge locations**.
    - You execute the function when the following events occur (**think from perspective of CF**):
        - When CF receives a request from a viewer (**viewer request**).
        - Before CF forwards a request to origin (**origin request**).
        - When CF receives a response from origin (**origin response**).
        - Before CF returns response to the viewer (**viewer response**).

# Notes from practice tests
- Use **CloudFront signed URL or signed cookies** feature to control access to the file
    - A signed URL includes additional information, for example, expiration date and time, that gives you more control over access to your content.
    - Here's an **overview of how you configure CloudFront and Amazon S3 for signed URLs or signed cookies** and how CloudFront responds when a user uses a signed URL to request a file:
        - In your CloudFront distribution, **specify one or more trusted key groups**, which contain the public keys that CloudFront can use to verify the URL signature. You use the corresponding private keys to sign the URLs.
            - To create signed URLs or signed cookies, you need a **signer**. A signer is either a **trusted key group** that you create in CloudFront, **or** an **AWS account** that contains a **CloudFront key pair**.
                - CloudFront **key pairs can only be created using the root user account** and hence is not a best practice to create CloudFront key pairs as signers).
                - When you use the **root user** to manage CloudFront key pairs, you can only have **up to two active CloudFront key pairs per AWS account**. Whereas, with CloudFront **key groups**, you can associate a higher number of public keys with your CloudFront distribution, giving you more flexibility in how you use and manage the public keys. By default, you can associate **up to four key groups with a single distribution, and you can have up to five public keys in a key group**.
            - **Each signer** that you use to create CloudFront signed URLs or signed cookies **must have a public–private key pair**. The **signer uses its private key to sign the URL or cookies**, and **CloudFront uses the public key to verify the signature**.
            - **Signers are associated with cache behaviors**. This allows you to require signed URLs or signed cookies for some files and not for others in the same distribution. A distribution requires signed URLs or cookies only for files that are associated with the corresponding cache behaviors.
            - Similarly, **a signer can only sign URLs or cookies for files that are associated with the corresponding cache behaviors**. 
        - Develop your application to determine whether a user should have access to your content and to create signed URLs for the files or parts of your application that you want to restrict access to.
        - A user requests a file for which you want to require signed URLs. Your application verifies that the user is entitled to access the file: they've signed in, they've paid for access to the content, or they've met some other requirement for access.
        - Your **application creates and returns a signed URL to the user**. The signed URL allows the user to download or stream the content.
    - This step is automatic; the user usually doesn't have to do anything additional to access the content. For example, if a user is accessing your content in a web browser, your application returns the signed URL to the browser. The browser immediately uses the signed URL to access the file in the CloudFront edge cache without any intervention from the user.
        - CloudFront uses the public key to validate the signature and confirm that the URL hasn't been tampered with. If the signature is invalid, the request is rejected. If the request meets the requirements in the policy statement, CloudFront does the standard operations: determines whether the file is already in the edge cache, forwards the request to the origin if necessary, and returns the file to the user.

- Use **CloudFront signed cookies** feature to control access to the file - CloudFront signed cookies allow you to control who can access your content when you don't want to change your current URLs or when you want to **provide access to multiple restricted files**, for example, all of the files in the subscribers' area of a website. Our requirement has only one file that needs to be shared and hence signed URL is the optimal solution.

- You **cannot directly integrate Cognito User Pools with CloudFront** distribution as **you have to create a separate Lambda@Edge function** to accomplish the authentication via Cognito User Pools.

- You can configure CloudFront to require that viewers use HTTPS to request your objects, so connections are encrypted when CloudFront communicates with viewers. You can also configure CloudFront to use HTTPS to get objects from your origin so connections are encrypted when CloudFront communicates with your origin. The process works as follows:
    1. A viewer submits an HTTPS request to CloudFront. There's some SSL/TLS negotiation here between the viewer and CloudFront. In the end, the viewer submits the request in an encrypted format.
    2. If the object is in the CloudFront edge cache, CloudFront encrypts the response and returns it to the viewer, and the viewer decrypts it.
    3. If the object is not in the CloudFront cache, CloudFront performs SSL/TLS negotiation with your origin and, when the negotiation is complete, forwards the request to your origin in an encrypted format.
    4. Your origin decrypts the request, encrypts the requested object, and returns the object to CloudFront.
    5. CloudFront decrypts the response, re-encrypts it, and forwards the object to the viewer. CloudFront also saves the object in the edge cache so that the object is available the next time it's requested.
    6. The viewer decrypts the response.

-  You can configure one or more cache behaviors in your CloudFront distribution to require HTTPS for communication between viewers and CloudFront. You also can configure one or more cache behaviors to allow both HTTP and HTTPS, so that CloudFront requires HTTPS for some objects but not for others. To implement this setup, you have to change the Origin Protocol Policy setting for the applicable origins in your distribution. If you're using the domain name that CloudFront assigned to your distribution, such as dtut0rial5d0j0.cloudfront.net, you change the Viewer Protocol Policy setting for one or more cache behaviors to require HTTPS communication. With this configuration, CloudFront provides the SSL/TLS certificate.

- You can't use a self-signed certificate for HTTPS communication between CloudFront and your origin.

- When you update existing files in a CloudFront distribution, AWS **recommends** that you include some sort of **version identifier** either in your file names or in your directory names to give yourself better control over your content. This identifier might be a date-time stamp, a sequential number, or some other method of distinguishing two versions of the same object. For example, instead of naming a graphic file image.jpg, you might call it image_1.jpg. When you want to start serving a new version of the file, you'd name the new file image_2.jpg, and you'd update the links in your web application or website to point to image_2.jpg. Alternatively, you might put all graphics in an images_v1 directory and, when you want to start serving new versions of one or more graphics, you'd create a new images_v2 directory, and you'd update your links to point to that directory. **With versioning, you don't have to wait for an object to expire in CF cache before CloudFront begins to serve a new version** of it, and you don't have to pay for object invalidation.