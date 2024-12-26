import unittest
from src.lambdas.hello_world.handler import HelloWorld, lambda_handler


class TestSuccess(unittest.TestCase):
    def setUp(self):
        self.handler = HelloWorld()

    def test_success(self):
        # Simulate a valid /hello GET request
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
        # Simulate an unsupported path and method
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
        # Test the lambda_handler with a valid request
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
        # Test the lambda_handler with an unsupported request
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
