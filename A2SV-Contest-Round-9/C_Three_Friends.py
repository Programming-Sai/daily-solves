'''
Solution is to minimise a and c to that they are closer to b
'''
from fprintx import printx


def check(a, b, c):
    offsets = [-1, 0, 1]
    best = float('inf')
    for _a in offsets:
        for _b in offsets:
            for _c in offsets:
                i, j, k = a+_a, b+_b, c+_c
                best = min(best, (abs(i - j) + abs(i - k) + abs(j - k)))
    return best


t = int(input())
for _ in range(t):
    a, b, c = list(map(int, input().split()))
    print(check(a, b, c))