"""Here one integer n is given. You need to write the complete function returnValueFunction that takes n as a parameter
 and uses the return keyword to return double the value of n."""


class Return_value_function:

    def __init__(self, a):
        self.a = a

    def print_value_function(self):
        return self.a * 2


if __name__ == "__main__":
    A = 2   # User can provide the option of giving any input
    return_function = Return_value_function(A)
    result = return_function.print_value_function()
    print(result)
