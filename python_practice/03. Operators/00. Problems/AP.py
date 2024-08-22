"""Given three integer, a,d and n. Where 'a' is the first term, d is the common difference of an A.P.
Calculate the nth term of A.P.  The nth term is given by an = a + (n-1)d """


class Arithmetic_progression:

    def __init__(self, a, d, n):
        self.a = a
        self.d = d
        self.n = n

    def arithmetic_p(self):
        return self.a + (self.n-1) * self.d


if __name__ == "__main__":
    A = 5
    D = 2
    N = 5
    ap = Arithmetic_progression(A, D, N)
    result = ap.arithmetic_p()
    print(result)
