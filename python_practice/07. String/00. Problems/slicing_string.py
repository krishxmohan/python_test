"""Given a string s, you need to slice it so that the output is a substring that contains all the characters except
first and last. The length of the s will be greater than 2."""


class String_slice:

    def __init__(self, s):
        self.s = s

    def print_sliced_string(self):
        return self.s[1: -1]


if __name__ == "__main__":
    S = "Hello"
    sliced_string = String_slice(S)
    result = sliced_string.print_sliced_string()
    print(result)
