class String_input:

    def __init__(self, a):
        self.a = a

    def input_str(self):
        return self.a


if __name__ == "__main__":
    A = input("Enter keyword: ")
    str_input = String_input(A)
    result = str_input.input_str()
    print(result)
