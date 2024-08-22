"""You are given a list that contains integers.
You need to print the elements of the list with in reverse order with a space between them."""


class List_traversal_reverse:

    def __init__(self, num):
        self.num = num

    def print_reverse_elements(self):
        print(self.num[::-1])


if __name__ == "__main__":
    Numbers = [324, 5, 2, 2]
    elements_in_list = List_traversal_reverse(Numbers)
    elements_in_list.print_reverse_elements()
