"""Given an integer S, write a program to print the square of size S using * character."""
#
# *  *  *  *  *
# *           *
# *           *
# *           *
# *  *  *  *  *


class Square:

    def __init__(self, s):
        self.s = s

    def print_square(self):
        for i in range(self.s):
            for j in range(self.s):
                if i == 0 or i == self.s - 1 or j == 0 or j == self.s - 1:
                    print('*', end='  ')
                else:
                    print(' ', end='  ')
            print()


if __name__ == "__main__":
    S = int(input("Enter n: "))
    hollow_square = Square(S)
    hollow_square.print_square()
