"""Given a string s, you need to reverse it."""


class Reverse_string:

    def __init__(self, s):
        self.s = s

    def print_reverse_string(self):
        return self.s[:: -1]


if __name__ == "__main__":
    S = "Hello"
    reverse = Reverse_string(S)
    result = reverse.print_reverse_string()
    print(result)
