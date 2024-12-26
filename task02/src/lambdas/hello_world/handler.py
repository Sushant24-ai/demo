import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class HelloWorld:
    def handle_request(self, event, context):
        path = event.get("path")
        method = event.get("httpMethod")
        
        logger.info(f"Handling request: path={path}, method={method}")

        # Check if the request matches the /hello GET endpoint
        if path == "/hello" and method == "GET":
            response = {
                "statusCode": 200,
                "body": json.dumps({
                    "message": "Hello from Lambda"
                })
            }
        else:
            response = {
                "statusCode": 400,
                "body": json.dumps({
                    "message": f"Bad request syntax or unsupported method. Request path: {path}. HTTP method: {method}"
                })
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
