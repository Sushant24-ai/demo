import unittest
import json
from src.lambdas.hello_world.handler import lambda_handler

class TestHelloWorld(unittest.TestCase):
    def test_invalid_method(self):
        event = {
            "path": "/unknown",
            "httpMethod": "DELETE",
            "requestContext": {
                "http": {
                    "method": "DELETE"
                }
            }
        }
        context = {}
        expected_response = {
            "statusCode": 400,
            "body": json.dumps({
                "message": "Bad request syntax or unsupported method. Request path: /unknown. HTTP method: DELETE"
            })
        }
        self.assertEqual(lambda_handler(event, context), expected_response)

if __name__ == "__main__":
    unittest.main()
