class Horizontal_print:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def horizontal(self):
        return self.a * self.b


if __name__ == "__main__":
    A = "#"
    B = int(input("Enter no: "))
    horizon = Horizontal_print(A, B)
    result = horizon.horizontal()
    print(result)
    print(result*2)
