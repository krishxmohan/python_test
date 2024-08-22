class Swap:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def swap_num(self):
        self.a, self.b = self.b, self.a
        return self.a, self.b


if __name__ == "__main__":
    num_a = int(input("Enter a: "))
    num_b = int(input("Enter b: "))
    sp = Swap(num_a, num_b)
    res_num_a, res_num_b = sp.swap_num()
    print(f'Before Swap num_a : {num_a}  num_b : {num_b}')
    print(f'After Swapping num_a : {res_num_a}  num_b : {res_num_b}')
