from fprintx import printx

import math

def check(x):
    possibilities = set(range(1, math.ceil(x ** (1/3))))
    for i in possibilities:
        print(i, math.floor((x-(i**3)**1/3)), x, i**3, x-(i**3))
        if math.floor((x-(i**3)**1/3)) in possibilities:
            print('YES')
            return
    print("NO")

check(2)


# t = int(input())
# for _ in range(t):
#     x = int(input())
#     check(x)