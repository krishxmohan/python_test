""" Given an integer s. Write a program to print the Inverted "Right angle triangle" wall.
The length of the perpendicular and base is s.  Use a single loop and string multiplication."""
# *  *  *  *  *
# *  *  *  *
# *  *  *
# *  *
# *
# NEED TO REVISIT


class Inverted_right_triangle:

    def __init__(self, s):
        self.s = s

    def print_inverted_triangle(self):
        for i in range(self.s):
            for j in range(self.s - i):
                print("*", end="  ")
            print()


if __name__ == "__main__":
    S = int(input("Enter n: "))
    inverted_triangle = Inverted_right_triangle(S)
    inverted_triangle.print_inverted_triangle()
