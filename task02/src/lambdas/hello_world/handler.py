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
        # Ensure we fetch the correct fields from the event
        path = event.get("rawPath", "")
        method = event.get("httpMethod", "")

        logger.info(f"Handling request: path={path}, method={method}")

        # Correctly respond to /hello with GET method
        if path == "/hello" and method == "GET":
            return {
                "statusCode": 200,
                "body": json.dumps({"message": "Hello from Lambda"})
            }

        # Default response for unsupported paths or methods
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": f"Bad request syntax or unsupported method. Request path: {path}. HTTP method: {method}"
            })
        }


def lambda_handler(event, context):
    """
    AWS Lambda entry point.
    """
    logger.info("Event received: %s", json.dumps(event, indent=2))
    handler = HelloWorld()
    return handler.handle_request(event, context)
