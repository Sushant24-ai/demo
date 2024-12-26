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


# Instantiate the handler object
HANDLER = HelloWorld()
