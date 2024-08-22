"""Given an integer s,  write a program to print a square wall of size s without using string multiplication.
Use nested loops instead. The * character will make up the wall."""
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
            for j in range(self.s):
                print("*", end="  ")
            print()


if __name__ == "__main__":
    S = int(input("Enter n: "))
    square_wall = Square(S)
    square_wall.print_square_wall()
