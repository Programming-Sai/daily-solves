n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
shortest_length = min(n, m)
shortest = []
if len(a) < len(b):
    shortest = a
else:
    shortest = b
i, j = 0, 0
res = []
while i < n and j < m:
    if a[i] < b[j]:
        res.append(a[i])
        i += 1
    else:
        res.append(b[j])
        j += 1

res.extend(a[i:])
res.extend(b[j:])
print(*res)