"""Given an integer s, write a program to print the square wall of size s using a single loop and string multiplication.
Use * character to make the wall."""
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *


class Square:

    def __init__(self, s):
        self.s = s

    def print_square_wall(self):
        for i in range(self.s):
            print('* ' * (self.s - 1) + '*')


if __name__ == "__main__":
    S = int(input("Enter n: "))
    square_wall = Square(S)
    square_wall.print_square_wall()
