# Elasticache

- Managed Redis or Memcache.
    - Memcache:
        - **Multi-node for sharding**
        - **No replication**
        - No persistance
        - No backup and restore
        - **Multithreaded**
        - Simple data types
    - Redis:
        - Complex data types
        - **No sharding (unless cluster mode is enabled)**
        - **Single threaded**
        - **Multi-AZ** with failover
        - **Read replicas** to scale reads
        - Data Durability (using Redis persistance functionalities)
        - Backup and restore features
- With an ALB + stickiness setup you can provide you with local session caching. There would be no need for a cache in that case, however elasticache will give you distributed session management. Each instance of app can access same cache.
- Caching strategies: 
    - **Lazy Loading**: Whenever your application requests data, it first makes the request to the ElastiCache cache. If the data exists in the cache and is current, ElastiCache returns the data to your application. If the data doesn't exist in the cache or has expired, your application requests the data from your data store. Your data store then returns the data to your application. Your application next writes the data received from the store to the cache. This way, it can be more quickly retrieved the next time it's requested.
    - **Write Through**: Add or update cache when database is updated. May be better from users perspective since client typically expects higher latency for write operations than read operations.
    - **Cache evictions and TTL**: Explicitly delete from cache, delete based on the least recently used (LRU) or by TTL. When an application attempts to read an expired key, it is treated as though the key is not found. The database is queried for the key and the cache is updated. This approach doesn't guarantee that a value isn't stale. However, it keeps data from getting too stale and requires that values in the cache are occasionally refreshed from the database.
- Redis **replication modes**:
    - **Cluster disabled**: **One primary** node and **up to 5 read replicas**. Async replication. One shard (all nodes have all data). **Multi-AZ** enabled by default for failover.
    - **Cluster enabled**: Partitioned across **shards** (scale write operations). **Each shard has one primary node and up to 5 replica nodes.** **Multi-AZ** capabilities. The **maximum is 500 nodes per cluster** (eg: if no read replicas are configured you can get up to 500 shards with one master each or 250 shards with one master and one replica per shard).

# Notes from practice tests
- Amazon ElastiCache makes it easy to deploy and manage a highly available and scalable in-memory data store in the cloud. Among the open source in-memory engines available for use with ElastiCache is Redis, which added powerful **geospatial capabilities** in its newer versions. You can leverage ElastiCache for Redis with cluster mode enabled to enhance reliability and availability with little change to your existing workload. **Cluster Mode comes with the primary benefit of horizontal scaling up and down of your Redis cluster**, with almost zero impact on the performance of the cluster. In short, it allows you to scale in or out the number of shards (horizontal scaling) versus scaling up or down the node type (vertical scaling). In a read-heavy workload, one can scale a single shard by adding read replicas, up to five, but a write-heavy workload can benefit from additional write endpoints when cluster mode is enabled.

- Redis **Geospatial** capabilities: Does not have to do with multi-region feature but with a **redis feature**. (don't mistake it with proximity caching for users, like CloudFront provides)

- Redis configurations:
![ElastiCache Redis Configurations](../media/elasticache-redis-configurations.png)

- https://aws.amazon.com/es/blogs/database/work-with-cluster-mode-on-amazon-elasticache-for-redis/

- All the nodes in a Redis cluster (cluster mode enabled or cluster mode disabled) must reside in the same region.

- While using Redis with cluster mode enabled, there are some limitations:
    - You cannot manually promote any of the replica nodes to primary.
    - Multi-AZ is required.
    - You can only change the structure of a cluster, the node type, and the number of nodes by restoring from a backup.

- Amazon ElastiCache offers fully managed Redis and Memcached for most demanding applications that require sub-millisecond response times. However, **Redis is the only service in Elasticache that supports replication**.

- Memcached is designed for simplicity while Redis offers a rich set of features that make it effective for a wide range of use cases. In terms of commands execution, **Redis is mostly a single-threaded server**. It is not designed to benefit from multiple CPU cores unlike Memcached, however, you can launch several Redis instances to scale out on several cores if needed.

- You can choose **Memcached over Redis** if you have the following requirements:
    - You need the **simplest model** possible.
    - You need to run **large nodes with multiple cores or threads**.
    - You need the ability to scale out and in, adding and removing nodes as demand on your system increases and decreases.
    - You need to cache objects, such as a database.