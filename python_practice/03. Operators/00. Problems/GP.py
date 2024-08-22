"""Given three integer, a, r and n. Where 'a' is the first term, r is the common ratio of a G.P.
Calculate the nth term of GP.  The nth term is given by an= a*rn-1"""


class Geometric_progression:

    def __init__(self, a, r, n):
        self.a = a
        self.r = r
        self.n = n

    def geometric_p(self):
        return self.a * self.r ** (self.n-1)


if __name__ == "__main__":
    A = 2
    R = 2
    N = 10
    gp = Geometric_progression(A, R, N)
    result = gp.geometric_p()
    print(result)
