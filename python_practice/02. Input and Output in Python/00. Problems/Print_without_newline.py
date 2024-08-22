class Print_without_newline:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_with_space(self):
        return f"{self.a} {self.b}"


if __name__ == "__main__":
    A = "Hello"
    B = "World"
    get_print_space = Print_without_newline(A, B)
    result = get_print_space.print_with_space()
    print(result)
