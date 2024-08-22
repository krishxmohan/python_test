"""You are given a list that contains integers. You need to return the length of the list."""


class List_length:

    def __init__(self, a):
        self.a = a

    def print_length(self):
        return len(self.a)


if __name__ == "__main__":
    A = [54, 43, 2, 1, 5]
    length_of_list = List_length(A)
    result = length_of_list.print_length()
    print(result)
