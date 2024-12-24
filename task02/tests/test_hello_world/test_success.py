import unittest
from src.lambdas.hello_world.handler import HelloWorld

class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        self.handler = HelloWorld()

    def test_success_hello(self):
        response = self.handler.handle_request("/hello", "GET")
        self.assertEqual(response["statusCode"], 200)
        self.assertEqual(response["message"], "Hello from Lambda")

    def test_bad_request_path(self):
        response = self.handler.handle_request("/invalid", "GET")
        self.assertEqual(response["statusCode"], 400)
        self.assertIn("Bad request syntax or unsupported method", response["message"])
        self.assertIn("/invalid", response["message"])

    def test_bad_request_method(self):
        response = self.handler.handle_request("/hello", "POST")
        self.assertEqual(response["statusCode"], 400)
        self.assertIn("Bad request syntax or unsupported method", response["message"])
        self.assertIn("POST", response["message"])

if __name__ == '__main__':
    unittest.main()
