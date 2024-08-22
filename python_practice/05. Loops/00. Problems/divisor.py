"""Given an integer N. Write a program to print all the divisors of N."""


class Divisor:

    def __init__(self, a):
        self.a = a

    def print_divisor(self):
        x = 1
        while x * x < self.a:
            if self.a % x == 0:
                print(x)
                print(self.a/x)
        x = x+1
        print(x)


if __name__ == "__main__":
    A = int(input("Enter n: "))
    calculate_divisor = Divisor(A)
    calculate_divisor.print_divisor()
    print(result)
