# Print from 1 to n in ascending order

def print_1_to_n(n: int):
    if n == 1:
        print(1)
        return
    print_1_to_n(n-1)
    print(n)

def print_n_to_1(n:int):
    if n == 1:
        print(1)
        return
    print(n)
    print_n_to_1(n-1)


# print_1_to_n(10)
print_n_to_1(10)