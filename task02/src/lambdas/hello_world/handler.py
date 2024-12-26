class HelloWorld:
    def handle_request(self, event, context):
        """
        Handle the Lambda function requests.

        Args:
            event (dict): The input event containing request details.
            context (dict): The Lambda context object.

        Returns:
            dict: Response object with status code and message.
        """
        # Extract the HTTP method and path from the event
        method = event.get("requestContext", {}).get("http", {}).get("method", "UNKNOWN")
        path = event.get("rawPath", "")

        # Check for the /hello GET resource
        if path == "/hello" and method == "GET":
            return {
                "statusCode": 200,
                "message": "Hello from Lambda"
            }

        # Return a 400 Bad Request response for all other endpoints
        return {
            "statusCode": 400,
            "message": f"Bad request syntax or unsupported method. Request path: {path}. HTTP method: {method}"
        }


# AWS Lambda entry point
def lambda_handler(event, context):
    """
    AWS Lambda entry point to invoke the HelloWorld class.

    Args:
        event (dict): The input event from API Gateway or Lambda URL.
        context (dict): The Lambda execution context.

    Returns:
        dict: Response object returned by the HelloWorld handler.
    """
    handler = HelloWorld()
    return handler.handle_request(event, context)
