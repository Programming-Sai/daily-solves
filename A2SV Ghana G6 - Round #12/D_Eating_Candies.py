from fprintx import printx


def check(n, w):
    l, r, max_len, a_eat, b_eat = 0 , n-1, 0, 0, 0
    while (l<r):
        a_eat += w[l]
        b_eat += w[r]

        if a_eat == b_eat:
            max_len = max(max_len, n-(r-l+1))




t = int(input())
for _ in range(t):
    n = int(input())
    w = list(map(int, input().split()))
    print(check(n, w))