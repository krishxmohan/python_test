class Multi_print:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def multiple_print(self):
        return self.a * self.b


if __name__ == "__main__":
    A = input("What do you want to print: ")
    B = int(input("Enter number: "))
    mul_print = Multi_print(A, B)
    result = mul_print.multiple_print()
    print(result)
