"""Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line."""


class While_loop:

    def __init__(self, n):
        self.n = n

    def while_loop_in_decreasing(self):
        result = ""
        i = self.n
        while i >= 0:
            result += (str(i))
            i = i-1
        return result


if __name__ == "__main__":
    N = int(input("Enter number: "))
    reversed_while_loop = While_loop(N)
    results = reversed_while_loop.while_loop_in_decreasing()
    print(results)
