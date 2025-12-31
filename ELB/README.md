# Elastic Load Balancers

- For **horizontal scaling** there are two solutions: ELBs and Auto Scaling (see Auto Scaling folder). IMPORTANT: Both of these solutions can be used for high availability. I.e: Multiple AZs (minimum 2). Both solution support multi AZ.
- By using an ELB we don't need to know about EC2s that support an app. Just get to it by a single entry point (with DNS) and also have benefits of **health checks** and **security at the ELB level**.
- Divides traffic coming from public internet into a private network where the app is hosted (it might even make since to implement **https termination** in the ELB and let other internal private traffic go as HTTP).
- In practice you create an ELB with a specific SG and then your **EC2 instances SG references the LB SG**. Eg: By opening EC2 SG on port 80 to the LB SG is the most secure way of ensuring only your ELB can access the EC2 instances.
- You configure load balancers to accept incoming traffic by specifying **one or more listeners**. A listener is a **process that checks for connection requests**. It is configured with a protocol and port number for connections **from clients to the load balancer**. Likewise, it is configure with a protocol and port number for connections **from the LB to targets**. The **rules** that you define for a listener determine **how the load balancer routes requests to its registered targets**. Each rule consists of a **priority**, one or more **actions**, and one or more **conditions**.
- Amazon DNS returns one or more IP addresses to the client. These are the IP addresses of the load balancer nodes for your LB (the client then decides to which IP to send the request).
- Each type of LB uses different algorithms to route traffic.
- Both internet facing or internal LBs **route traffic to targets using private IP addresses**, Therefore your **targets do not need public IPs** to receive requests from external/internal clients.
- A Load Balancer can target EC2 instances **only within an AWS Region**.
- Types of LBS:
    - **Classic - CLB (v1)**:
        - **TCP (LAyer 4), HTTP and HTTPS (Layer 7).**
        - **Each CLB has its own DNS name**
        - You configure port and protocol for external communication and internal communication.
        - You attach multiple EC2 instances in different AZs to a single CLB (**each EC2 must be running the same app**).
        - Health checks are TCP or HTTP based.
    - **App Load Balancer - ALB (v2)**:
        - **Layer 7 ONLY (HTTP/s and WebSockets).**
        - It load balances to machines organized in target groups.
        - Supports load balancing into **many apps within a single EC2 instance** (eg: Containers). This can be done because it has a **port mapping feature**. If we used CLB we would need one EC2 per app instance.
        - You add EC2s to target group and then make ALB reference the target group.
        - **Health checks are done at the Target group level**.
        - App EC2 does NOT directly see clients IP address. To do so we need to use a special HTTP header called **x-forwarded-for-proto/x-forwarded-for**.
        - You can create **routing** tables to route to different Target Groups based on:
            - **Url path**
            - **Host name**
            - **Query string**
        - **Max number of routing rules for ALB is 75**
        - ALB are great for microservice apps and container based applications.
        - **ALBs can sit in front of EC2 instances, ECS tasks, lambda functions and private Ip addresses** (eg: register private ip addresses of **on premise servers** on a TG and let the ALB route traffic into it).
        - When you create a target group, you specify its **target type**, which determines the type of target you specify when registering targets with this target group. After you create a target group, you cannot change its target type. The following are the possible target types:
            - **Instance** - The targets are specified by **instance ID** ( traffic is routed to instances using the primary private IP address specified in the primary network interface for the instance)
            - **IP** - The targets are **IP addresses** (If you specify targets using IP addresses, you can route traffic to an instance using any private IP address from **one or more network interfaces**. This **enables multiple applications on an instance to use the same port**)
            - **Lambda** - The target is a Lambda function
                - ALB provides two advanced options that you may want to configure when you use ALBs with AWS Lambda: support for **multi-value headers** and **health check** configurations. You can set up these options in Target Groups section on the Amazon EC2 console. After you enable multi-value headers, the headers and query parameters exchanged between the load balancer and the Lambda function use **arrays instead of strings.**
                - For example, suppose the client supplies a query string like: `?name=foo&name=bar`, if you’ve enabled multi-value headers, ALB supplies these duplicate parameters in the event object as: `‘name’: [‘foo’, ‘bar’]`. ALB applies the same processing to duplicate HTTP headers. If you do not enable multi-value header syntax and a header or query parameter has multiple values, the load balancer uses the last value that it receives.
        - **You can not specify publicly routable IP addresses to an ALB**: When the target type is IP, you can specify IP addresses from specific CIDR blocks only. You can't specify publicly routable IP addresses.
        - Its **obligatory to have ALB running in minimum two AZs** for high availability.
        - **Port mapping**:
            - When you launch a container, ports are automatically mapped from the containers port (eg: 80) to a randomly generated host port. Once that is done, ALB is smart enough to listen for these randomly generated ports and forwards traffic to it.
            - To enable this feature, its important to **leave "Host port" option empty in container so a random port can be assigned**.
        - **ALB access logs**:
            - Elastic Load Balancing provides access logs that capture detailed **information about requests sent to your load balancer**. Each log contains information such as the time the request was received, the client's IP address, latencies, request paths, and server responses. You can use these access logs to analyze traffic patterns and troubleshoot issues. Access logging is an **optional feature** of Elastic Load Balancing that is **disabled by default**. They are **streamed to s3 bucket as compressed files**. You can disable access logging at any time. Each file is **automatically encrypted using SSE-S3**. Yo are only charged for s3 bucket storage.
        - **ALB request tracing**:
            - You can use request tracing to track HTTP requests. The load balancer **adds a header with a trace identifier to each request it receives**. Request tracing will not help you to analyze latency specific data.
        - Support for **websockets**: Application Load Balancers provide native support for WebSockets. You can upgrade an existing HTTP/1.1 connection into a WebSocket (ws or wss) connection by using an HTTP connection upgrade. When you upgrade, the TCP connection used for requests (to the load balancer as well as to the target) becomes a persistent WebSocket connection between the client and the target through the load balancer.
    - **Network Load Balancers - NLB (v2)**:   
        - Load balance at **Layer 4 (TCP / UDP).**
        - **Lower latency** (millions of req per second), more than ALB.
        - Has **one static IP per AZ** **(different than CLB and ALB that only have a static Host name, Ip may vary)**. This means that you can use NLB to whitelist the specific static IP. Clients know that that IP is trusted since its the NLB. You have one static IP address because AWS actually creates one network interface for each enabled AZ.
        - **Supports assigning Elastic IP**.
        - It also works with Target groups. Inbound comes in Layer 4 but after that redirection to specific TGs can be done in other Layer (HTTP for example).
        - **NLBs can send traffic to EC2s in TG, Ip addresses** (eg: register private ip addresses of on premise servers on a TG and let the NLB route traffic into it). **It can event redirect to an ALB**, for example if we want static IP but also want ALB for redirection rules for microservice app.
        - For NLB, the EC2 **instances that sit behind it don't see traffic coming from the NLB but from the outside clients**. This means that if your app uses HTTP, you need to open SG rules of EC2 instances to accept TCP port 80 from anywhere.
        - Incoming connections remain unmodified, so application software **need not support X-Forwarded-For** (applications behind NLB access client IP directly).
        - **NLBs decide routing based on network layer variables (like IP and Ports). It does not have any awareness about app layer variables (like content type, cookies, headers, user location, etc). Only decides upon network layer info.**
        - NLB **cannot ensure availability of application**. It can an most perform basic ICMP pings to app or complete the three way TCP handshake with the app. ALBs go much deeper into health checks because they can perform actual HTTP requests like GETS, POSTS, etc to the running app.
    - **Gateway Load Balancer - GWLB:**
        - Deploy, scale, and manage a fleet of **3rd party network virtual appliances** in AWS.
        - You would use a GWLB if you wanted to have **all traffic of your network to go through a firewall, intrusion detection and prevention systems, deep packet inspection systems, payload manipulation systems at the network level.**
        - By modifying route tables inside your VPC, all traffic coming un VPC goes to GWLB. Then the **GWLB spreads traffic to our 3rd party network virtual appliances running on EC2** instances that are in a TG. I**f traffic is accepted it returns to GWLB and finally that is forwarded to yor EC2 running the apps (lo usas como filtro).**
        - GWLB **operates at level 3 (IP packets)**.
        - Uses the **GENEVE protocol on port 6081**.
        - GWLB can **send traffic to EC2s and private ip addresses** (same as ALB and NLB)
- **Sticky sessions:**
    - Client always **redirects to one instance by leveraging cookies** (once cookie is generated, all subsequent request by client are sent with this cookie so LB knows where to redirect traffic).
    - This **may imbalance traffic** between your EC2 instances.
    - In **ALB stickiness is at the target group level, on classic its to specific instances**.
    - Two types of cookies:
        - **Application-based cookies**: **Generated by YOUR app**. It can include any business related custom attributes in it. The cookie name must be specified individually for each target group. You can delegate the creation of this cookie to the LB itself (if no custom attribute is needed).
        - **Duration based cookies**: **Generated by LB**. It has a specific duration specified by the LB.
- **Cross-Zone Load Balancing:**
    - When you enable an Availability Zone for your load balancer, Elastic Load Balancing creates a load balancer node in the Availability Zone. **If you register targets in an Availability Zone but do not enable the Availability Zone, these registered targets do not receive traffic.** 
    - **After you disable an Availability Zone, the targets in that Availability Zone remain registered with the load balancer. However, even though they remain registered, the load balancer does not route traffic to them.**
    - Each LB will distribute evenly across all registered AZs. LB in AZ1 distributes traffic to other AZs and the same for the LBs in other AZ.
    - The nodes for your load balancer distribute requests from clients to registered targets. **When cross-zone load balancing is enabled, each load balancer node distributes traffic across the registered targets in all enabled Availability Zones**. When **cross-zone load balancing is disabled**, each load balancer node distributes traffic **only across the registered targets in its Availability Zone**.
    - Cross-Zone LB by Type:
        - CLB: **Disabled by default**. No charge if enabled for inter AZ data transfers. When data goes from one AZ to another, then you will be charged for it. But if you enable it for CLB then you wont be charged for it.
        - ALB: **Always on**. No charges for inter AZ data transfers.
        - NLB: **Disabled by default**. You pay money if you enable cross-zone. You DO pay for inter AZ data transfers ("regional data transfers may apply when cross-zone is enabled").
- **SSL/TLS Certificates**:
    - TLS is actually the newer version of SSL.
    - Issued by CA (Certificate Authority)
    - Connect to LB with SSL and then use HTTP to redirect to specific EC2s/TGs.
    - SSL Server Name Indication: If I have an ALB or NLB that serves multiple websites that haver different certificates. How does the server know what certificate to load? The client specifies the hostname of target server in the initial handshake. **Multiple certificates are supported by ALB, NLB and CloudFront**. For CLB you can only have one certificate. By using SNI you are able to have multiple TGs for different websites using different SSL certificates.
- **Connection draining:**
    - **Time to complete "in-flight" requests while the instance is being de-registered or is unhealthy.**
    - The idea is that once an instance is being de-registered in the TG, the LB does not send any more requests to that instance and lets it finish up what it was processing before de-registering it.
    - Its important to know hoy much time each request takes to know whats the ideal timeout to set.
    - When EC2 is in draining mode. The **existing connections will be waited for the duration of the connection draining timeout** to be completed (by **default its 300 seconds**).
    - When connection draining is enabled and configured, the process of de-registering an instance from a ELB gains an additional step. For the duration of the configured timeout, the LB will allow existing in-flight requests made to an instance to complete but will not send any new requests to it. Once timeout is reached, andy existing connections will be forcibly closed.
    

# Notes from practice tests
- ALB listeners
    - Before you start using your Application Load Balancer, you must add one or more listeners.
    - A listener is a process that checks for connection requests, using the protocol and port that you configure. The rules that you define for a listener determine how the load balancer routes requests to its registered targets.
    - **Each listener has a default rule, and you can optionally define additional rules**. Each rule consists of a priority, one or more actions, and one or more conditions.
    - Each rule has a priority. Rules are **evaluated in priority order, from the lowest value to the highest value.**
    - Rules have rule **actions and rule conditions**. Each **rule action has a type, an order, and the information required to perform the action**. Each **rule condition has a type and configuration information**.
    - Rule action types:
        - **authenticate-cognito:** Use Amazon Cognito to authenticate users
        - **authenticate-oidc:** Use an identity provider that is compliant with OpenID Connect (OIDC) to authenticate users.
        - **fixed-response:** Return a custom HTTP response
        - **forward:** Forward requests to the specified target groups
            - **If you specify multiple target groups for a forward action, you must specify a weight for each target group.**
            - Each **target group weight is a value from 0 to 999**.
            - Sticky session: When the load balancer first routes a request to a weighted target group, it generates a **cookie named AWSALBTG** that encodes information about the selected target group, encrypts the cookie, and includes the cookie in the response to the client.
        - **redirect**: Redirect requests from one URL to another
    - **Each rule must include exactly one of the following actions: forward, redirect, or fixed-response, and it must be the last action to be performed.**
    - Rule **condition types**
        - **host-header**: Route based on the **host name** of each request.
        - **http-header**: Route based on the **HTTP headers** for each request.
        - **http-request-method**: Route based on the **HTTP request method** of each request
        - **path-pattern**: Route based on **path patterns** in the request URLs.
        - **query-string**: Route based on **key/value pairs or values in the query strings.**
            - route requests based on key/value pairs or values in the query string.
            - The query string component starts after the first "?" in a URI. Typically query strings contain key-value pairs separated by a delimiter "&". 
            - Example of query string condition. The following condition is satisfied by requests with a query string that includes either a key/value pair of "version=v1" or any key set to "example".
            ```json
            [
            {
                "Field": "query-string",
                "QueryStringConfig": {
                    "Values": [
                        {
                            "Key": "version",
                            "Value": "v1"
                        },
                        {
                            "Value": "*example*"
                        }
                    ]
                }
            }
            ]
            ```
        - **source-ip**: Route based on the **source IP address of each request.**
    - **Each rule can optionally include up to one of each of the following conditions: host-header, http-request-method, path-pattern, and source-ip. Each rule can also optionally include one or more of each of the following conditions: http-header and query-string.**

- The Load Balancer generates the **HTTP 503**: **Service unavailable** error when the target groups for the load balancer have **no registered targets**.

- **Connection timeout default is 10 seconds**

- Authentication in Load Balancer
    - You can configure an Application Load Balancer to **securely authenticate users** as they access your applications.
    - **Offload the work of authenticating users to your load balancer**
    - Options:
        - Authenticate users through an identity provider (IdP) that is OpenID Connect (**OIDC**) compliant.
        - Authenticate users through **social IdPs**, such as Amazon, Facebook, or Google, through the user pools supported by Amazon Cognito.
        - Authenticate users through **corporate identities**, using SAML, LDAP, or Microsoft AD, through the user pools supported by Amazon Cognito.
    - The authenticate-cognito and authenticate-oidc action types are supported only with HTTPS listeners.
    - The load balancer sends a session cookie to the client to maintain authentication status. This cookie always contains the secure attribute, because **user authentication requires an HTTPS listener**. This cookie contains the SameSite=None attribute with CORS (cross-origin resource sharing) requests.
    ![ALB authentication](../media/alb-authentication.png)
    1. User sends an HTTPS request to a website hosted behind an Application Load Balancer. When the conditions for a rule with an authenticate action are met, the load balancer **checks for an authentication session cookie in the request headers**.
    2. **If the cookie is not present**, the load balancer **redirects** the user to the IdP authorization endpoint so that the IdP can authenticate the user.
    3. After the user is authenticated, the **IdP sends the user back to the load balancer with an authorization grant code**.
    4. The load balancer **presents the authorization grant code to the IdP token endpoint**.
    5. Upon receiving a valid authorization grant code, the **IdP provides the ID token and access token to the Application Load Balancer**.
    6. The Application Load Balancer then **sends the access token to the user info endpoint**.
    7. The user info endpoint **exchanges the access token for user claims**.
    8. The **Application Load Balancer redirects the user with the AWSELB authentication session cookie to the original URI**. Because most browsers limit the cookie size to 4K, the load balancer shards a cookie that is greater than 4K in size into multiple cookies. If the total size of the user claims and access token received from the IdP is greater than 11K bytes in size, the load balancer returns an HTTP 500 error to the client and increments the ELBAuthUserClaimsSizeExceeded metric.
    9. The Application Load Balancer **validates the cookie and forwards the user info to targets** in the X-AMZN-OIDC-* HTTP headers set.
    10. The target **sends a response back to the Application Load Balancer**.
    11. The Application Load Balancer sends the **final response to the user**.