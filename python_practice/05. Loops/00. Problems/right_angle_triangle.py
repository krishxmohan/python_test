"""Given an integer s. Write a program to print the Right angle triangle wall.The length of perpendicular and base is s.
Use single loop and string multiplication."""
# *
# *  *
# *  *  *
# *  *  *  *
# *  *  *  *  *


class Right_triangle:

    def __init__(self, s):
        self.s = s

    def print_right_triangle(self):
        for i in range(1, self.s + 1):
            print(''.join(" * " * i))


if __name__ == "__main__":
    S = int(input("Enter n: "))
    right_angle = Right_triangle(S)
    right_angle.print_right_triangle()
