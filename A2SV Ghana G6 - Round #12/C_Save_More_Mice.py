
from fprintx import printx


def check(n, k, x):
    x.sort()
    cat = save = 0
    for i in range(len(x)-1, -1, -1):
        if x[i] < cat:
            break
        save += 1
        cat += n - x[i]
    return save


n, k, x = 10, 6, list(set([8, 7, 5, 4, 9, 4]))
# n, k, x = 2, 8,list(set( [1]*8))
# print(check(n, k, x))


for _ in range(int(input())):
    n, k = map(int, input().split())
    x = list(set(map(int, input().split())))
    print(check(n, k, x))