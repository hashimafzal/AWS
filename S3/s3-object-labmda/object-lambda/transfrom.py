import boto3
import requests

# This function capitalizes all text in the original object
def lambda_handler(event, context):
    object_context = event["getObjectContext"]
    # Get the presigned URL to fetch the requested original object 
    # from S3. A presigned URL that the Lambda function can use to 
    # download the original object from the supporting access point.
    # By using a presigned URL, the Lambda function doesn't need to
    # have Amazon S3 read permissions to retrieve the original 
    # object and can only access the object processed by each invocation.
    s3_url = object_context["inputS3Url"]
    # Extract the route and request token from the input context
    request_route = object_context["outputRoute"] # routing token that is added to the S3 Object Lambda URL when the Lambda function calls WriteGetObjectResponse to send back the transformed object.
    request_token = object_context["outputToken"] # A token used by S3 Object Lambda to match the WriteGetObjectResponse call with the original caller when sending back the transformed object.
    
    # Get the original S3 object using the presigned URL
    response = requests.get(s3_url)
    original_object = response.content.decode("utf-8")

    # Transform all text in the original object to uppercase
    # You can replace it with your custom code based on your use case
    transformed_object = original_object.upper()

    # Write object back to S3 Object Lambda
    s3 = boto3.client('s3')
    # The WriteGetObjectResponse API sends the transformed data
    # back to S3 Object Lambda and then to the user
    s3.write_get_object_response(
        Body=transformed_object,
        RequestRoute=request_route,
        RequestToken=request_token)

    # Exit the Lambda function: return the status code  
    return {'status_code': 200}                                      