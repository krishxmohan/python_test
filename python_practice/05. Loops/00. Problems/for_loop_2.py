"""You are given a String S, you need to print its characters at even indices(index starts at 0)."""


class For_loop:

    def __init__(self, s):
        self.s = s

    def print_even_indices(self):
        result = []
        for i in range(len(self.s)):
            if i % 2 == 0:
                result.append((i, self.s[i]))
        return result


if __name__ == "__main__":
    S = "Geeks"
    print_for_loop = For_loop(S)
    results = print_for_loop.print_even_indices()
    print(results)
