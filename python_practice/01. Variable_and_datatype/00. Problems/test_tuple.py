class Check_tuple:

    def __init__(self, a):
        self.a = a

    def check_distinct(self):
        return len(self.a) == len(set(self.a))


if __name__ == "__main__":
    A = (1, 2, 3, 4, 5, 4)
    dist_tuple = Check_tuple(A)
    result = dist_tuple.check_distinct()
    print(result)
