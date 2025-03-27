import json

def lambda_handler(event, context):
    """
    AWS Lambda function that returns a formatted Hello World message
    """
    message = {
        'message': 'Hello, World!!',
        'event': event,  # Includes the incoming event data
        'function_name': context.function_name,  # Name of the Lambda function
        'function_version': context.function_version,  # Version of the function
        'invoked_function_arn': context.invoked_function_arn  # ARN of the function
    }
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(message)
    } 