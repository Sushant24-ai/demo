import json
import logging

# Set up basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class HelloWorld:
    def handle_request(self, event, context):
        """
        Handles incoming requests and returns the appropriate response.
        """
        # Extract path and method from the event
        path = event.get("rawPath", "")
        method = event.get("requestContext", {}).get("http", {}).get("method", "")

        logger.info(f"Handling request: path={path}, method={method}")

        # Check if the request matches the /hello GET endpoint
        if path == "/hello" and method == "GET":
            response = {
                "statusCode": 200,
                "message": "Hello from Lambda"
            }
        else:
            response = {
                "statusCode": 400,
                "message": f"Bad request syntax or unsupported method. Request path: {path}. HTTP method: {method}"
            }

        logger.info(f"Response: {response}")
        return response


def lambda_handler(event, context):
    """
    AWS Lambda entry point.
    """
    logger.info("Event received: %s", json.dumps(event, indent=2))
    handler = HelloWorld()
    return handler.handle_request(event, context)
