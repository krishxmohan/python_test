"""Given four inputs that are stored in variables a,b,c, and d.
You need to write an expression to evaluate the following formula. Use integer division.
The expression should be a single statement."""


class Formulae:

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def evaluate(self):
        results = ((self.a + self.b)//self.c) + self.d
        return results


if __name__ == "__main__":
    A = 10
    B = 4
    C = 7
    D = 9
    eval_formulae = Formulae(A, B, C, D)
    result = eval_formulae.evaluate()
    print(result)
