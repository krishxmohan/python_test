"""You are given a list that contains integers. You need to return the sum of the list."""


class List_sum:

    def __init__(self, a):
        self.a = a

    def print_list_sum(self):
        return sum(self.a)


if __name__ == "__main__":
    A = [54, 43, 2, 1, 5]
    sum_of_list = List_sum(A)
    result = sum_of_list.print_list_sum()
    print(result)
