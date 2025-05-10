from fprintx import printx


def check(n, a):
    l = 0
    r = n-1
    length = n
    while l < r:
        if a[l] != a[r]:
            # print(a[l:r+1], l, r)
            l += 1
            r -= 1
            length -= 2
        else:
            break

    return length




t = int(input())
for _ in range(t):
    n = int(input())
    a = list(input())
    # print(*a)
    print(check(n, a))