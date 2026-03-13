n, m = map(int, input().split())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))
res = []
if len(a) < len(b):
    start_arr = a
    other_arr = b
else: 
    start_arr = b
    other_arr = a

for i in range(len(start_arr)):
    if a[i] < b[i]:
        res.append(a[i])
        res.append(b[i])
    else:
        res.append(b[i])
        res.append(a[i])

res.extend(other_arr[i+1:])
print(*res)