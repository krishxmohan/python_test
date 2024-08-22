class Input_int:

    def __init__(self, a):
        self.a = a

    def int_input(self):
        return self.a + 10


if __name__ == "__main__":
    A = int(input("Enter no: "))
    inp_int = Input_int(A)
    result = inp_int.int_input()
    print(result)
