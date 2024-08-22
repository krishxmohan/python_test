class Get_union:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def union_set(self):
        return self.a.union(self.b)


if __name__ == "__main__":
    set_a = {2, 5, 6}
    set_b = {1, 4, 3, 2}
    set_uni = Get_union(set_a, set_b)
    result = set_uni.union_set()
    print(result)
