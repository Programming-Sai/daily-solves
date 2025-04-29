from fprintx import printx


def check(n, r):
    count = 0
    max_count = 0
    for i in range(n):
        count += (r[i])
        max_count = max(max_count, count)
    return max_count


t=int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    print(check(n, r) + check(m, b))