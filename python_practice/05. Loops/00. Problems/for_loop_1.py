"""You are given a number n, you need to print its multiplication table in a single line."""


class For_loop:

    def __init__(self, n):
        self.n = n

    def print_for_loop(self):
        results = ""
        for i in range(1, 11):
            results = results + str(i * self.n) + ", "
        return results


if __name__ == "__main__":
    Num = int(input("Enter number: "))
    print_loop = For_loop(Num)
    result = print_loop.print_for_loop()
    print(result)
