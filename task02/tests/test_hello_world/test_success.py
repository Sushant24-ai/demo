import unittest
from src.lambdas.hello_world.handler import HelloWorld, lambda_handler

class TestSuccess(unittest.TestCase):
    def setUp(self):
        # Set up a HelloWorld instance for testing
        self.handler = HelloWorld()

    def test_success(self):
        """
        Test that a valid GET request to '/hello' returns the correct response.
        """
        event = {
            "rawPath": "/hello",
            "requestContext": {
                "http": {
                    "method": "GET"
                }
            }
        }
        context = {}
        expected_response = {
            "statusCode": 200,
            "message": "Hello from Lambda"
        }
        self.assertEqual(self.handler.handle_request(event, context), expected_response)

    def test_bad_request(self):
        """
        Test that an invalid request (wrong path or method) returns a 400 response.
        """
        event = {
            "rawPath": "/invalid",
            "requestContext": {
                "http": {
                    "method": "POST"
                }
            }
        }
        context = {}
        expected_response = {
            "statusCode": 400,
            "message": "Bad request syntax or unsupported method. Request path: /invalid. HTTP method: POST"
        }
        self.assertEqual(self.handler.handle_request(event, context), expected_response)

    def test_lambda_handler_success(self):
        """
        Test the AWS Lambda entry point with a valid event.
        """
        event = {
            "rawPath": "/hello",
            "requestContext": {
                "http": {
                    "method": "GET"
                }
            }
        }
        context = {}
        expected_response = {
            "statusCode": 200,
            "message": "Hello from Lambda"
        }
        self.assertEqual(lambda_handler(event, context), expected_response)

    def test_lambda_handler_bad_request(self):
        """
        Test the AWS Lambda entry point with an invalid event.
        """
        event = {
            "rawPath": "/unknown",
            "requestContext": {
                "http": {
                    "method": "DELETE"
                }
            }
        }
        context = {}
        expected_response = {
            "statusCode": 400,
            "message": "Bad request syntax or unsupported method. Request path: /unknown. HTTP method: DELETE"
        }
        self.assertEqual(lambda_handler(event, context), expected_response)


if __name__ == "__main__":
    unittest.main()
