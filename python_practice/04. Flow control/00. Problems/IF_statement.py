"""Given a number, you have to use the if statement to print "Big" (without quotes) if the given number is greater than
100. The statement "Number" (without quotes) will be printed regardless."""


class If_statement:

    def __init__(self, num):
        self.num = num

    def print_if_statement(self):
        if self.num > 100:
            return "Big Number"
        else:
            return "Number"


if __name__ == "__main__":
    Num = int(input("Enter number: "))
    if_else = If_statement(Num)
    result = if_else.print_if_statement()
    print(result)
