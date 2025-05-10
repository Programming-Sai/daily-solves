from fprintx import printx


def check(n, a):
    sum_ = 0
    ones_count = a.count(1)
    for num in a:
        sum_ += ones_count + (1 if num == 0 else -1)
    return sum_


t = int(input())
for _ in range(t):
    n = int(input())
    a = list((map(int, input())))
    print(check(n, a))