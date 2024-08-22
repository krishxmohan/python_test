"""Given three inputs that are stored in the variables a, b, and c.
You need to print 'a' a times and 'b' b times  in a single line separated by c."""


class Int_str:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def print_integer_n_times(self, num=None):
        res = ''
        for i in range(num):
            res += str(num)
        return res

    def main(self):
        print(self.print_integer_n_times(self.a) + self.c + self.print_integer_n_times(self.b))


if __name__ == "__main__":
    A = 6
    B = 4
    C = "&"
    int_str = Int_str(A, B, C)
    int_str.main()
