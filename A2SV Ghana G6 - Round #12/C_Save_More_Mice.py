
from fprintx import printx


def check(n, k, x):
    x.sort()
    l = cat = save = 0
    r = len(x)-1
    while l <= r:
        printx(l, r, cat, save, x, widths=[3])
        x[r] += 1
        if x[r] == n:
            r -= 1
            save += 1
        cat += 1
        if x[l] == cat:
            l += 1
            
    return save


n, k, x = 10, 6, list(set([8, 7, 5, 4, 9, 4]))
# n, k, x = 2, 8,list(set( [1]*8))
print(check(n, k, x))


# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     x = list(set(map(int, input().split())))
#     print(check(n, k, x))