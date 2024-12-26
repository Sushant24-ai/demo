class HelloWorld:
    def handle_request(self, event, context):
        """
        Handles incoming requests and returns the appropriate response.
        """
        path = event.get("rawPath", "")
        method = event.get("requestContext", {}).get("http", {}).get("method", "")

        if path == "/hello" and method == "GET":
            return {
                "statusCode": 200,
                "message": "Hello from Lambda"
            }
        else:
            return {
                "statusCode": 400,
                "message": f"Bad request syntax or unsupported method. Request path: {path}. HTTP method: {method}"
            }


def lambda_handler(event, context):
    """
    AWS Lambda entry point.
    """
    handler = HelloWorld()
    return handler.handle_request(event, context)
