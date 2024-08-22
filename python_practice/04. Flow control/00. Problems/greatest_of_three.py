"""Given three numbers a, b, and c; you need to find which is the greatest of them all."""


class Greatest_of_three:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def print_greatest_of_three(self):
        return max(self.a, self.b, self.c)


if __name__ == "__main__":
    A = int(input("Enter 1st number: "))
    B = int(input("Enter 2nd number: "))
    C = int(input("Enter 3rd Number: "))
    print_max = Greatest_of_three(A, B, C)
    result = print_max.print_greatest_of_three()
    print("The greatest number is", result)
