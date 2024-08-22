class Add_print:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add_and_print(self):
        return self.a + self.b


if __name__ == "__main__":
    A = "Geeks"
    B = "World"
    add = Add_print(A, B)
    result = add.add_and_print()
    print(result)
