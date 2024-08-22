"""Here two integers a and b are given. The take input and their values are passed as arguments to the function
argumentFunction. The argumentFunction is responsible for the syntax print(a+b). You need to write this function."""


class Argument_function:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_argument(self):
        return self.a + self.b


if __name__ == "__main__":
    A = 2    # User can input any integer
    B = 3    # User can input any integer
    argument_with_function = Argument_function(A, B)
    result = argument_with_function.print_argument()
    print(result)
