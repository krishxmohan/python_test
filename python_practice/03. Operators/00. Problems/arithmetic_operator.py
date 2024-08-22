""" You are given two integer variables x and y. You need to perform the following operations:

p = x+y : Addition
q = x-y : Subtraction
r = x*y :Multiplication
s = x/y : Float Division
t = x//y : Int Division
u = x%y : Modulo
v = x**y : Power"""


class Arithemetic_operators:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def operators(self):
        p = self.x + self.y
        q = self.x - self.y
        r = self.x * self.y
        s = self.x / self.y
        t = self.x // self.y
        u = self.x % self.y
        v = self.x ** self.y
        return p, q, r, s, t, u, v


if __name__ == "__main__":
    X = int(input("Enter first number: "))
    Y = int(input("Enter second number: "))
    arithmetic = Arithemetic_operators(X, Y)
    result = arithmetic.operators()
    print(" ".join(map(str, result)))
