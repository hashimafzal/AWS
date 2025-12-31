# AppSync

- Managed services that uses GraphQL.
- You create and give access to a **GraphQL API**.
- Supports **combining data from multiple sources (NOSQL, relational databases, HTTP APIs, DynamoDB, aurora, custom sources with Lambda)**.
- Support for retrieving data using **WebSockets** and MQTT on WebSocket.
- For mobile apps, AppSync is a newer version of Cognito Sync which helps you with **local data access and data synchronization.**
- It all starts with uploading a graphQL schema and resolver.
![App Sync overview](../media/appsync-overview.png)
- Security:
    - API_KEYS
    - AWS_IAM
    - **OPENID_CONNECT**
    - AMAZON_COGNITO_USER_POOLS
- AWS AppSync is quite similar with Amazon Cognito Sync which is also a service for synchronizing application data across devices. It enables user data like app preferences or game state to be synchronized as well however, the key difference is that, it also extends these capabilities by allowing multiple users to synchronize and collaborate in real time on **shared data**.
