"""Given a string s, you need to perform the following operation.
1. Capitalize the first letter and print.
2. Convert the whole string to uppercase and print."""


class Change_case:

    def __init__(self, s):
        self.s = s

    def print_after_changing(self):
        return self.s.title(), self.s.upper()


if __name__ == "__main__":
    S = "hello"
    case = Change_case(S)
    title_case, upper_case = case.print_after_changing()
    print(title_case)
    print(upper_case)
