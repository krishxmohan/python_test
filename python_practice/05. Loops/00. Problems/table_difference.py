"""Given two number n1 and n2, n1 > n2. Find the differences between mathematical tables of n1 and n2."""


class Table_diff:

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def table_n1(self):
        res_1 = []
        for i in range(1, 11):
            res_1.append(i * self.n1)
        return res_1

    def table_n2(self):
        res_2 = []
        for i in range(1, 11):
            res_2.append(i * self.n2)
        return res_2

    def print_table_difference(self):
        res_1 = self.table_n1()
        res_2 = self.table_n2()
        difference = []
        for i in range(len(res_2)):
            difference.append(res_2[i]-res_1[i])
        return difference


if __name__ == "__main__":
    N1 = int(input("Enter number: "))
    N2 = int(input("Enter number: "))
    table_difference = Table_diff(N1, N2)
    results = table_difference.print_table_difference()
    print(results)
