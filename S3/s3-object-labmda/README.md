# [Tutorial: Transforming data for your application with S3 Object Lambda](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tutorial-s3-object-lambda-uppercase.html)

With S3 Object Lambda, you can add your own code to process data retrieved from S3 before returning it to an application. Specifically, you can configure an AWS Lambda function and attach it to an S3 Object Lambda access point. When an application sends standard S3 GET requests through the S3 Object Lambda access point, the specified Lambda function is invoked to process any data retrieved from an S3 bucket through the supporting S3 access point. Then, the S3 Object Lambda access point returns the transformed result back to the application.

Notes: 
- The access point must be in the same AWS Region as the objects that you want to transform.
- When you're writing a Lambda function for use with an S3 Object Lambda access point, the function is based on the input event context that S3 Object Lambda provides to the Lambda function. The event context provides information about the request being made in the event passed from S3 Object Lambda to Lambda
- To enable your Lambda function to provide customized data and response headers to the GetObject caller (the client app wanting to access s3), your Lambda function's execution role must have IAM permissions to call the WriteGetObjectResponse API.
- An S3 Object Lambda access point provides the flexibility to invoke a Lambda function directly from an S3 GET request so that the function can process data retrieved from an S3 access point. When creating and configuring an S3 Object Lambda access point, you must specify the Lambda function to invoke and provide the event context in JSON format as custom parameters for Lambda to use.
- A payload is optional JSON text that you can provide to your Lambda function as input for all invocations coming from a specific S3 Object Lambda access point. To customize the behaviors for multiple Object Lambda access points that invoke the same Lambda function, you can configure payloads with different parameters, thereby extending the flexibility of your Lambda function.
- When you request to retrieve a file through your S3 Object Lambda access point, you make a GetObject API call to S3 Object Lambda. S3 Object Lambda invokes the Lambda function to transform your data, and then returns the transformed data as the response to the standard S3 GetObject API call.

# Questions
- Difference between "Object Lamda Access Point" and "Access Point"?
    - With S3 Access Points, customers can create unique access control policies for each access point to easily control access to shared datasets.
    - An Object Lambda access point is associated with exactly one standard access point and thus one Amazon S3 bucket. 
    - When creating a "Object Lamda Access Point" you specify an "Access Point" as a supporting "Access Point".
