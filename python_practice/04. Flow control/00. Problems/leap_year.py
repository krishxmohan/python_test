"""Given an integer y. Check whether it can represent a leap year or not."""


class Leap_year:

    def __init__(self, year):
        self.year = year

    def check_leap_year(self):
        if self.year % 4 == 0 and self.year % 100 != 0:
            return True
        elif self.year % 400 == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    Year = int(input("Enter Year: "))
    check_leap = Leap_year(Year)
    result = check_leap.check_leap_year()
    print(result)
