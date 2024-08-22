"""You are given a list that contains integers.
You need to print the elements of the list with a space between them."""


class List_traversal:

    def __init__(self, num):
        self.num = num

    def print_elements(self):
        for i in self.num:
            print(i, end=" ")


if __name__ == "__main__":
    Numbers = [54, 43, 2, 1, 5]
    elements_in_list = List_traversal(Numbers)
    elements_in_list.print_elements()
