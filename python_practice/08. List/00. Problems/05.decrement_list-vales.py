"""You are given a list that contains integers.
You need to decrement each element of the list by 1 and return the list."""


class Decrement_list:

    def __init__(self, a):
        self.a = a

    def print_decrement_list(self):
        for i in self.a:
            return i-1


if __name__ == "__main__":
    A = [324, 5, 2, 2]
    decrement = Decrement_list(A)
    result = decrement.print_decrement_list
    print(result)
