import unittest
from src.lambdas.hello_world.handler import HANDLER  # Import the instantiated HANDLER

class TestSuccess(unittest.TestCase):
    def setUp(self):
        self.handler = HANDLER  # Use the HANDLER instance

    def test_success(self):
        """
        Test a successful request to the /hello GET resource.
        """
        event = {
            "rawPath": "/hello",
            "requestContext": {"http": {"method": "GET"}}
        }
        context = {}
        expected_response = {
            "statusCode": 200,
            "message": "Hello from Lambda"
        }
        self.assertEqual(self.handler.handle_request(event, context), expected_response)

    def test_bad_request(self):
        """
        Test an invalid request to a different path or method.
        """
        event = {
            "rawPath": "/invalid",
            "requestContext": {"http": {"method": "POST"}}
        }
        context = {}
        expected_response = {
            "statusCode": 400,
            "message": "Bad request syntax or unsupported method. Request path: /invalid. HTTP method: POST"
        }
        self.assertEqual(self.handler.handle_request(event, context), expected_response)


if __name__ == "__main__":
    unittest.main()
