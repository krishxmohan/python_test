"""You are given a number, and you have to print your answer according to the following:
If the number is divisible by 3, you print "Fizz" (without quotes)
If the number is divisible by 5, you print "Buzz" (without quotes)
If the number is divisible by both 3 and 5, you print "FizzBuzz" (without quotes)
In any other case, you print the number itself """


class Fizzbuzz:

    def __init__(self, num):
        self.num = num

    def print_fizzbuzz(self):
        if self.num % 3 == 0 and self.num % 5 == 0:
            return "FizzBuzz"
        elif self.num % 3 == 0:
            return "Fizz"
        elif self.num % 5 == 0:
            return "Buzz"
        else:
            return self.num


if __name__ == "__main__":
    A = int(input("Enter a number: "))
    get_if_elif = Fizzbuzz(A)
    result = get_if_elif.print_fizzbuzz()
    print(result)
