from fprintx import printx


def check(n, m, k, a, b):
    a = sorted(a)
    b = sorted(b)
    c = ""
    # printx(n, m, k, a, b, widths=[3])
    range_n = min(n, m)
    i = ca = cb = j = 0
    # print(a[0] < b[0], range_n)
    while i < n and j < m:
        if (a[i] < b[j] and ca < k) or cb == k:
            c += a[i]
            i += 1
            ca += 1
            cb = 0
        else:
            c += b[j]
            j += 1
            cb += 1
            ca = 0
    return c



# n, m, k = 5, 9, 3
# a, b = "caaca", "bedededeb"

n, m, k = 7, 7, 1
a="noskill"
b="wxhtzdy"
# print(check(n, m, k, a, b))


t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    a = input()
    b = input()
    print(check(n, m, k, a, b))