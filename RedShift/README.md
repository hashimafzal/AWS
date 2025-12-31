# Redshift

- Amazon Redshift is a fully managed, petabyte-scale data warehouse service in the AWS Cloud. An Amazon Redshift data warehouse is a collection of computing resources called nodes, which are organized into a group called a cluster. Each cluster runs an Amazon Redshift engine and contains one or more databases.
- Amazon Redshift supports client connections with many types of applications, including business intelligence (BI), reporting, data, and analytics tools. 
- At the data ingestion layer, different types of data sources continuously upload structured, semistructured, or unstructured data to the data storage layer. This data storage area serves as a staging area that stores data in different states of consumption readiness. An example of storage might be an Amazon Simple Storage Service (Amazon S3) bucket.
- Amazon Redshift is based on PostgreSQL. Amazon Redshift and PostgreSQL have a number of very important differences that you need to take into account as you design and develop your data warehouse applications. For information about how Amazon Redshift SQL differs from PostgreSQL
- At the optional data processing layer, the source data goes through preprocessing, validation, and transformation using extract, transform, load (ETL) or extract, load, transform (ELT) pipelines. These raw datasets are then refined by using ETL operations. An example of an ETL engine is AWS Glue.
-  At the data consumption layer, data is loaded into your Amazon Redshift cluster, where you can run analytical workloads.
![Redshift Overview](../media/redshift-overview.png)
- Concepts:
    - Cluster: A cluster is composed of one or more compute nodes. The compute nodes run the compiled code. If a cluster is provisioned with two or more compute nodes, an additional leader node coordinates the compute nodes. The leader node handles external communication with applications, such as business intelligence tools and query editors. Your client application interacts directly only with the leader node. The compute nodes are transparent to external applications.
    - Databases: User data is stored in one or more databases on the compute nodes. Your SQL client communicates with the leader node, which in turn coordinates running queries with the compute nodes.
![Redshift Internals](../media/redshift-internals.png)
