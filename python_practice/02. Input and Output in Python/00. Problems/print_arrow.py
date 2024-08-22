class Arrow:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def arrow_print(self):
        return self.a

    def print_gap(self):
        for i in range(self.b):
            print(' ')

    def construct_arrow(self):
        for i in range(self.b):
            if i == 1:
                print(' '*self.c, self.arrow_print())
                self.print_gap()
            else:
                print(self.arrow_print())
                self.print_gap()


if __name__ == "__main__":
    A = '--------------->'
    B = 3
    C = 10
    print_arrow = Arrow(A, B, C)
    print_arrow.construct_arrow()
