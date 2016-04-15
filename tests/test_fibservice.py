#!/usr/bin/env python
import unittest
from app.services.fibservice import Fibonacci


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.fib1 = Fibonacci(5)
        self.fib2 = Fibonacci(-5)
        self.fib3 = Fibonacci("adsf")

    def tearDown(self):
        pass

    # Check the fib calculation
    def test_fib_to(self):
        fib1_value = {'Fibonacci': [0, 1, 1, 2, 3]}
        self.assertEqual(self.fib1.fib_to(), fib1_value)
        fib2_value = {'Fibonacci': [0, 1]}
        self.assertEqual(self.fib2.fib_to(), fib2_value)

    # validate the fib input
    def test_user_input(self):
        self.assertTrue(self.fib1.valid_user_input())
        self.assertFalse(self.fib2.valid_user_input())
        self.assertFalse(self.fib3.valid_user_input())


if __name__ == '__main__':
    unittest.main()
