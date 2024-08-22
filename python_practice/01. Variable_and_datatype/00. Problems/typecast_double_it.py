class Bodmas:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        if self.a > self.b:
            return self.a - self.b
        else:
            return f"ERROR: {self.a} is smaller than {self.b}. It should be vice versa"

    def multiply(self):
        return self.a * self.b


if __name__ == '__main__':
    num_a = int(input('Enter first Number: '))
    num_b = int(input("Enter second Number: "))
    BD = Bodmas(num_a, num_b)
    res_add, res_sub, res_mul = BD.addition(), BD.subtraction(), BD.multiply()
    print(res_add, res_sub, res_mul)
