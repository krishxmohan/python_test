class Multi_print_space:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_input(self):
        for i in range(self.b):
            print(self.a, end=', ')


if __name__ == "__main__":
    A = 'Hello'
    B = int(input("Enter no of you wanna print: "))
    mul_print = Multi_print_space(A, B)
    mul_print.print_input()
