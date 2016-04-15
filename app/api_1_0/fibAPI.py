#!/usr/bin/env python
from flask import jsonify
from app.services.fibservice import Fibonacci
from app.api_1_0 import api


@api.route('/fib/<fib_number>')
def get_fib(fib_number):
    fib = Fibonacci(fib_number)
    if not fib.valid_user_input():
        return "please input a integer and large than 2"
    fib_result = fib.fib_to()
    return jsonify(fib_result)
