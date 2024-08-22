"""Given three positive integers a, b and c. Your task is to perform some bitwise operations on them as given below:
1. d = a ^ a
2. e = c ^ b
3. f = a & b
4. g = c | (a ^ a)
5. e = ~ e
Note: ^ is for xor.
The output is d e f g """


class Bitwise:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def bitwise_operator(self):
        d = self.a ^ self.a
        e = self.c ^ self.b
        f = self.a & self.b
        g = self.c | (self.a ^ self.a)
        e = ~ e
        return d, e, f, g


if __name__ == "__main__":
    A = 1
    B = 2
    C = 3
    bit_operator = Bitwise(A, B, C)
    result = bit_operator.bitwise_operator()
    print(result)
