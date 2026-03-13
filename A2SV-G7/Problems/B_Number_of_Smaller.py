n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res, l = [], 0
for num in b:
    while l < n and a[l] < num:
        l += 1
    res.append(l)
print(*res)
