"""Given an integer s. Write a program to print the Right angle triangle. The length of the perpendicular and base is s.
  Use single loop and string multiplication."""


class Right_triangle:

    def __init__(self, s):
        self.s = s

    def print_right_triangle(self):
        # for i in range(self.s):
        #     for j in range(self.s):
        #         if i == 0 or j == self.s - 1 and i == 1 and j == 1:
        #             print('*', end='  ')
        #         print()

        pass


if __name__ == "__main__":
    S = int(input("Enter n:"))
    right_angle_triangle = Right_triangle(S)
    right_angle_triangle.print_right_triangle()
