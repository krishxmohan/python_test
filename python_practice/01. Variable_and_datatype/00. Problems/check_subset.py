'''Given two sets A and B. check whether A is subset of B ?
A is subset of B, if all elements of a set A are present in another set B.'''


class Subset:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def check_subset(self):
        return self.a.issubset(self.b)


if __name__ == "__main__":
    set_a = {1, 4, 3}
    set_b = {1, 4, 3, 2}
    ss = Subset(set_a, set_b)
    result = ss.check_subset()
    print(result)
