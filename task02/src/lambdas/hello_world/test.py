import boto3

def create_function_url(function_name):
    lambda_client = boto3.client('lambda')
    
    try:
        response = lambda_client.create_function_url_config(
            FunctionName=function_name,
            AuthType='NONE'
        )
        print(f"Function URL created: {response['FunctionUrl']}")
        return response
        
    except lambda_client.exceptions.ResourceConflictException:
        print(f"Function URL already exists for {function_name}")
    except Exception as e:
        print(f"Error creating function URL: {str(e)}")

# Example usage
function_name = 'cmtr-b1f07e8d-hello_world-test'
create_function_url(function_name)