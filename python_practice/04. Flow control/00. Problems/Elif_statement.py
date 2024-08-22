"""Given a number, you have to use if, elif, else conditional statements according to the following:
if number is greater than 100: Print "Big" (without quotes)
else if number is smaller than 10: Print "Small" (without quotes)
else: Print "Number" (without quotes)"""


class Elif_statement:

    def __init__(self, num):
        self.num = num

    def print_elif(self):
        if self.num > 100:
            return "Big number"
        elif self.num < 10:
            return "Small number"
        else:
            return "Number"


if __name__ == "__main__":
    A = int(input("Enter a number: "))
    get_elif = Elif_statement(A)
    result = get_elif.print_elif()
    print(result)
