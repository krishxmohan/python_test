"""Given a number, you have to use the if statement to print "Big" (without quotes)
if the given number is greater than 100, and use the else statement to print "Number" (without quotes)
when the number is smaller than or equal to 100."""


class Else_statement:

    def __init__(self, num):
        self.num = num

    def print_else_statement(self):
        if self.num > 100:
            return "Big Number"
        else:
            return "Number"
 

if __name__ == "__main__":
    Num = int(input("Enter number: "))
    if_else = Else_statement(Num)
    result = if_else.print_else_statement()
    print(result)
