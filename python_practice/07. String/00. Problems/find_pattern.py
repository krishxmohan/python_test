"""Given a string s, and a pattern p. You need to find if p exists in s or not and return the starting index of p in s.
If p does not exist in s then -1 will be returned. Here p and s both are case-sensitive."""


class Find_pattern:

    def __init__(self, s, p):
        self.s = s
        self.p = p

    def print_pattern(self):
        index = self.s.find(self.p)     # Find the starting index of the pattern
        return index        # The find method returns -1 if the pattern is not found


if __name__ == "__main__":
    S = "Hello"
    P = "you"
    pattern = Find_pattern(S, P)
    result = pattern.print_pattern()
    print(result)
