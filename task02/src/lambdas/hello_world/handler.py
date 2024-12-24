from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('HelloWorld-handler')


import json

class HelloWorld:
    def handle_request(self, event, context):
        """
        Handle the incoming event and route based on the HTTP path and method.

        Args:
            event: The event data passed to the Lambda function.
            context: The context object provided by AWS Lambda.

        Returns:
            dict: A response dictionary with statusCode and message.
        """
        # Safely extract the path and method from the event with defaults
        path = event.get("rawPath", "/")
        method = event.get("requestContext", {}).get("http", {}).get("method", "GET")

        if path == "/hello" and method == "GET":
            # Return success for /hello
            return {
                "statusCode": 200,
                "message": "Hello from Lambda"
            }
        else:
            # Return 400 Bad Request for other paths or methods
            return {
                "statusCode": 200,
                "message": f"Bad request syntax or unsupported method. Request path: {path}. HTTP method: {method}"
            }

    

HANDLER = HelloWorld()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
