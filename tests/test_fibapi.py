#!/usr/bin/env python
import json
import unittest
from flask import url_for
from app import create_app


class FibAPITestCase(unittest.TestCase):
    # Initial UT
    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    # de-construt UT
    def tearDown(self):
        self.app_context.pop()

    def test_get_fib(self):
        response1 = self.client.get(url_for('api.get_fib', fib_number=5))
        self.assertTrue(response1.status_code == 200)
        json_response = json.loads(response1.data.decode('utf-8'))
        compare_value1 = [0, 1, 1, 2, 3]
        self.assertTrue(json_response.get('Fibonacci', 0) == compare_value1)

        response2 = self.client.get(url_for('api.get_fib', fib_number=-5))
        self.assertTrue(response2.status_code == 200)
        self.assertEqual(response2.data.decode('utf-8'), "please input a integer and large than 2")

        response3 = self.client.get(url_for('api.get_fib', fib_number="asdf"))
        self.assertTrue(response3.status_code == 200)
        self.assertEqual(response3.data.decode('utf-8'), "please input a integer and large than 2")


if __name__ == '__main__':
    unittest.main()
