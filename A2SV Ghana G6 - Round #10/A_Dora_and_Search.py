from fprintx import printx

def check(n, a):
    l, r, min_, max_ = 0, n-1, 1, n

    while l < r:
        if a[l] == min_:
            l += 1
            min_ += 1
        elif a[l] == max_:
            l += 1
            max_ -= 1
        elif a[r] == min_:
            r -= 1
            min_ += 1
        elif a[r] == max_:
            r -= 1
            max_ -= 1
        else:
            break
    if l >= r:
        print(-1)
    else:
        print(l+1, r+1)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    (check(n, a))