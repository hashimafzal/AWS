# Route 53

- Amazon Route 53 is a highly available and scalable Domain Name System (DNS) web service. You can use Route 53 to perform three main functions in any combination: domain registration, DNS routing, and health checking.
- You can have a public domain names or private ones for your private apps (e.g: internal apps) within a single VPC.
- Domain Registration
    - Chose name + Top level domain
    - When you register a domain with Route 53, the service automaticaly makes itself the DNS service for the domain by doing the following:
        - Creates a hosted zone (container of records)
        - Assign a set of 4 name servers to the hosted zone. When someone uses a browser to access your website, these servers tell browser where to find the resources.
        - Gets the name servers from the hosted zone and adds them to the domain.
- DNS players:
    - User: Wants to register a domain and TLD. User sends this to registrar.
    - Registrar: Authorized by ICANN to register specific TLDs.
    - Registry: Company that sells domain registrations. They are specific to a TLD and container a DB of domains, their owners and WHOIS.
- Once you have a hosted name you can add records (by adding record sets).
    - Eg:
        - You register a domain by "francocanova.com"
        - Ypu add a record to this "hosted zone" called "myfirstrecord" and assign it to IP 1.22.33.44
            - Hosted Zone: A container for records, which include information about how you want to route traffic for a domain (such as example.com) and all of its subdomains (such as www.example.com, retail.example.com, and seattle.accounting.example.com). A hosted zone has the same name as the corresponding domain. For example, the hosted zone for example.com might include a record that has information about routing traffic for www.example.com to a web server that has the IP address 192.0.2.243, and a record that has information about routing email for example.com to two email servers, mail1.example.com and mail2.example.com. Each email server also requires its own record.
        - Now if you perform an "nslookup myfirstrecord francocanova.com" (Nslookup is a command-line tool that lets you test and troubleshoot Domain Name System (DNS) resolution).
        - You get that its being resolved as 11.22.33.44.
- DNS records TTL:
    - Its a way for clients to cache response of DNS query. So DNS servers are not overloaded.
    - Browser will cache that DNS-Ip mapping for specified TTL.
    - Updating an IP on Route 53 does not mean that all clients IPs will be updated immediately.
    - If you put a TTL on a record you can verify the time its being cached using a "dig" command on the hostname (it will show you how long its been cached on your PC).
    - Setting TTL affects how much queries go to DNS servers.
- After you create a hosted zone for your domain, such as example.com, you create records to tell the Domain Name System (DNS) how you want traffic to be routed for that domain. Each record includes the name of a domain or a subdomain, a record type (for example, a record with a type of MX routes email), other information applicable to the record type (for MX records, the host name of one or more mail servers and a priority for each server), and a value (closely related to type, its the identifier of the resource to redirect to). The name of each record in a hosted zone must end with the name of the hosted zone. For example, the example.com hosted zone can contain records for www.example.com and accounting.tokyo.example.com subdomains, but cannot contain records for a www.example.ca subdomain.

- Understand what are the most common record types
    - A: Route to resource using an IPv4 address in dotted decimal notation.
    - AAAA: IPv6 address in colon-separated hexadecimal format.
    - CNAME: Maps DNS queries fot the name of the current record to another domain of another subdomain.
    - PTR: Map IP address to corresponding domain name.
    - NS: Identifies the name server for the hosted zone. Use when you need the servers from one hosted zone redirect to another hosted zone to resolve a particular IP. E.g: You can create a subdomain (acme.example.com) and use that hosted zone to route traffic for the subdomain and its subdomains (subdomain.acme.example.com).
    - MX: Specifies the names of your mail servers and if you have two or more mail servers, the priority order. Each value for an MX record contains two values, priority and domain name.
    - SOA (Start of Authority): Provides information about a domain and the corresponding Amazon Route 53 hosted zone (contact, refresh time, retry intervals, TTL).
    - TXT: Contains one or more strings that are enclosed in double quotation marks. When you use the simple routing policy, include all values for a domain or subdomain in the same TXT record.
- CNAME vs Alias:
    - A CNAME record maps DNS queries for the name of the current record, such as acme.example.com, to another domain (example.com or example.net) or subdomain (acme.example.com or zenith.example.org). CNAME records can be used to map one domain name to another. Although you should keep in mind that the DNS protocol does not allow you to create a CNAME record for the top node of a DNS namespace, also known as the zone apex. For example, if you register the DNS name example.com, the zone apex is example.com. You cannot create a CNAME record for example.com, but you can create CNAME records for www.example.com, newproduct.example.com, and so on.
    - An Alias points a host name to a AWS resource. They also let you route traffic from one record in a hosted zone to another record. Unlike a CNAME record, you can create an alias record at the top node of a DNS namespace, also known as the zone apex.
    - They differ in that alias has to point to AWS resource while CNAME can be any hostname. If you have a root domain then you have to use an alias. If its a non root domain you can use either. Its almost always the case you are going to use alias since you are typically pointing to aa AWS resource.
- Routing Policies:
    - Simple: One simple DNS policy can return more than one IP associated to a hostname. The client select one randomly and goes there (client side load balancing).
    - Weighted: Balance request to different IPs based on a % of requests. ITs another way of associating same hostname to different IPs. From the clients perspective, it only sees one IP, not multiple ones (no client side load balancing). Use to test different versions of apps.
    - Latency: Based solely on latency. You create different record sets linking the same hostname with different resources and select latency option for every one of them. If your infra is in multiple regions, ypu can improve performance for your users by serving their requests from the AWS region with the lowest latency. You can test this using VPN and testing connection to different resources depending on where in the world you connect from.
    - Failover: You have one primary and one secondary. When you create the record you associate the primary one with a health check. If that one fails, then traffic is sent to the secondary one (specified through another record that in this case does not need any associated health checks). Both primary and secondary use same hostname.
    - Geolocation: Not latency but solely based on location. Tg: You have a legal requirement that people in france should not be able to access your web, you would then use this policy. Also use for serving websites in different languages for example. If you create different records for overlapping geographic locations, priority goes to the smallest geographic location. Geolocation routing lets you choose the resources that serve your traffic based on the geographic location of your users, meaning the location that DNS queries originate from. For example, you might want all queries from Europe to be routed to an ELB load balancer in the Frankfurt region. You can also use geolocation routing to restrict distribution of content to only the locations in which you have distribution rights You can create a default record that handles both queries from IP addresses that aren't mapped to any location and queries that come from locations that you haven't created geolocation records for. If you don't create a default record, Route 53 returns a "no answer" response for queries from those locations.
    - Multi-value: Improvement over client load balancing simple routing policy (one hostname returns multiple IPs and lets browser choose one randomly), because we get health checks on each record. Up to 8 healthy records are returned for each multi-value query. If one instance is unhealthy then that ip is not returned to the client. If you don't associate a health check to a multi-value answer record, Route 53 assumes its healthy.
- Just like LBS, Route 53 has health checks. They can be directly linked to the record set and DNS queries will change behavior opf Route 53 automatically.
- Health checks:
    - To create one you specify the IP, protocol, interval and failure threshold and how you want to be notified.
    - You can configure a health check to the health of other health checks, so you can be notified when specific number of resources (such as 2 out of 5) are unavailable. You can also create a health check to check status of a CW alarm sop that you can be notified on the basis of a broad range of criteria, not just wether a resource is responding to requests or not.
- ELB vs Route 53:
    - ELB:
        - Distributes traffic among multiple AZs
        - Unhealthy instances are terminated from target group
    - Route 53:
        - Can route traffic across regions (in a diagram it would sit before an ELB)
        - Removes unhealthy resources from its list (does not remove instances per se). However DNS is cached so unhealthy targets will still be in clients caches.






