"""Given an integer N find the sum of the first N natural number."""


class Natural_numbers:

    def __init__(self, n):
        self.n = n

    def print_natural_numbers(self):
        return self.n*(self.n+1)//2


if __name__ == "__main__":
    N = int(input("Enter n: "))
    sum_of_natural_numbers = Natural_numbers(N)
    result = sum_of_natural_numbers.print_natural_numbers()
    print(result)
