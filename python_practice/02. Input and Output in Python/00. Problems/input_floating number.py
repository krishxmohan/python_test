"""Given a floating number, you need to input it.
The floating number will then be printed after multiplying it by 10 """


class Float:

    def __init__(self, a):
        self.a = float(a)

    def floating(self):
        return self.a * 10


if __name__ == "__main__":
    A = input("Enter floating no: ")
    flt = Float(A)
    result = flt.floating()
    print(result)
