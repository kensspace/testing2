#!/usr/bin/env python


class Fibonacci:

    def __init__(self, fib_number):
        self.fib_number = fib_number

    def __del__(self):
        pass

    # Validate user input to integer
    def valid_user_input(self):
        try:
            return int(self.fib_number) > 2
        except ValueError:
            return False

    # Calculate fib and convert to json
    def fib_to(self):
        fibs = [0, 1]
        for i in range(2, int(self.fib_number)):
            fibs.append(fibs[-1] + fibs[-2])
        json_fib = {'Fibonacci': fibs}
        return json_fib
