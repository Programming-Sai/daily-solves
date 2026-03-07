n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = []
x, y = 0, 0

while y < m:
    while x < n and a[x] < b[y]:
        x += 1
    res.append(x)
    y += 1
print(" ".join([str(c) for c in res]))