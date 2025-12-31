# EventBridge

- Evolution of CW Events
- We all have a default Event Bus
- We can create:
    - Partner Event Bus: Receive events from third party SaaS services.
    - Custom Event Bus: For custom apps.
- Buses can be accessed by other aws accounts using a resource based policy. 
- You can archive events
- You define Rules to process the events (destinations). A single rule can route to multiple destinations. A rule can also modify the event in some way before sending it to destinations.
- Schema Registry and Code Bindings:
    - EventBridge an analyze events and infer a schema
    - This schema can later generate code for your application that knows in advance how the data is structured in th event bus.
    - Schemas can be versioned.
    - Code bindings help create a strongly typed object in the code to create events and perform validations before sending.