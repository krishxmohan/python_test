class Print_without_space:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def without_space(self):
        return f"{self.a}{self.b}"


if __name__ == "__main__":
    A = "Hello"
    B = "World"
    get_without_space = Print_without_space(A, B)
    result = get_without_space.without_space()
    print(result)
