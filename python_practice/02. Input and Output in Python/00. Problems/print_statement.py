class Print_statement:

    def __init__(self, a):
        self.a = a

    def print(self):
        return self.a


if __name__ == "__main__":
    A = "Hello_World"
    prnt = Print_statement(A)
    result = prnt.print()
    print(result)
