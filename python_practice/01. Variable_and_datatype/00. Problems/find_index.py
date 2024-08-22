class Find_index:

    def __init__(self, a, x):
        self.a = a
        self.x = x

    def get_index(self):
        results = self.a.index(self.x)
        return results


if __name__ == "__main__":
    A = (1, 2, 3, 4, 5)
    X = int(input("Enter no from tuple: "))
    index = Find_index(A, X)
    result = index.get_index()
    print(result)
