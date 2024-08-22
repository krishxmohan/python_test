class Print_with_seperator:

    def __init__(self, a, b, seperator):
        self.a = a
        self.b = b
        self.seperator = seperator

    def print_seperator(self):
        return f"{self.a}{self.seperator}{self.b}"


if __name__ == "__main__":
    A = "Hello"
    B = "World"
    sep = "@"
    print_sep = Print_with_seperator(A, B, sep)
    result = print_sep.print_seperator()
    print(result)
