class Concatenate:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def concatenate_int(self):
        return str(self.a) + str(self.b)


if __name__ == "__main__":
    int_a = input("Enter a: ")
    int_b = input("Enter b: ")
    con_int = Concatenate(int_a, int_b)
    res_a, res_b = con_int.concatenate_int()
    print(res_a, res_b)
