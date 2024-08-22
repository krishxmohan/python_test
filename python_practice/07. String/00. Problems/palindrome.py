"""Given a string s, you need to check if it is palindrome or not. A palindrome is a string that reads the same from
front and back. Ignore the case in this question."""


class Check_palindrome:

    def __init__(self, s):
        self.s = s.lower()      # Adding lower() to make it case insensitive

    def print_palindrome(self):
        if self.s == self.s[:: -1]:     # Check if the string is equal to its reverse
            return True
        else:
            return False


if __name__ == "__main__":
    S = "nitIn"
    palindrome = Check_palindrome(S)
    result = palindrome.print_palindrome()
    print(result)
