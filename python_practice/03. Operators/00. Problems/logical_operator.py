"""Logical operators and, or, not are used in condition checking. Like a and b checks if both a and b are True.
First 'a' is checked then b is checked. a or b checks if either of a or b is True.
If one is True; it doesn't check for the other.
not a complements the boolean value of a
Note: 0 and empty string are False and all other values are True.
In this question you basically need to do
a and b
a or b
not a """


class Logical_operator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def logical_and(self):
        return self.x and self.y

    def logical_or(self):
        return self.x or self.y

    def logical_not_x(self):
        return not self.x

    def logical_not_y(self):
        return not self.y


if __name__ == "__main__":
    X = 0
    Y = 2
    logic = Logical_operator(X, Y)
    result_and = logic.logical_and()
    result_or = logic.logical_or()
    result_not_x = logic.logical_not_x()
    result_not_y = logic.logical_not_y()

    print("Logical AND:", result_and)
    print("Logical OR:", result_or)
    print("Logical NOT of X:", result_not_x)
    print("Logical NOT of Y:", result_not_y)
