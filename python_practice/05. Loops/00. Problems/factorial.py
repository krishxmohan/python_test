"""Given an integer N. Write a program to return the factorial of N."""

import math


class Factorial:

    def __init__(self, a):
        self.a = a

    def print_factorial(self):
        return math.factorial(self.a)


if __name__ == "__main__":
    A = int(input("Enter n: "))
    get_factorial = Factorial(A)
    result = get_factorial.print_factorial()
    print(result)
