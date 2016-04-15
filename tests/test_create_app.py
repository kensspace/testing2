import unittest
from app import create_app


class TestCreate_app(unittest.TestCase):
    # Initial UT
    def setUp(self):
        pass

    # de-construt UT
    def tearDown(self):
        pass

    def test_create_app(self):
        self.test_app = create_app("testing")
        self.test_app_context = self.test_app.app_context()
        self.test_app_context.push()
        self.test_client = self.test_app.test_client()
        self.test_app_context.pop()

        self.dev_app = create_app("development")
        self.dev_app_context = self.dev_app.app_context()
        self.dev_app_context.push()
        self.dev_client = self.dev_app.test_client()
        self.dev_app_context.pop()

if __name__ == '__main__':
    unittest.main()
