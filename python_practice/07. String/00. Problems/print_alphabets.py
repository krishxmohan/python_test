"""Given two char c1 and c2.  you need to print all the alphabet starting from c1 to c2 in a single line."""


class Alphabets:

    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

    def print_c1_c2(self):
        start = ord(self.c1)  # Convert the first character to its ASCII value
        end = ord(self.c2)    # Convert the second character to its ASCII value
        alphabets = [chr(i) for i in range(start, end + 1)]  # Create a list of characters from ASCII values
        return " ".join(alphabets)  # Join the characters in the list with a space and return as a single string


if __name__ == "__main__":
    C1 = "a"
    C2 = "z"
    print_alphabets = Alphabets(C1, C2)
    result = print_alphabets.print_c1_c2()
    print(result)
