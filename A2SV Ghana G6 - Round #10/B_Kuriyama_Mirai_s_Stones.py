from fprintx import printx


def check(n, v, m, q):
    pass


n = int(input())
v = list(map(int, input().split()))
m = int(input())
q = []
for _ in range(m):
    q.append(list(map(int, input().split())))
check(n, v, m, q)