n = int(input())
a = list(map(int, input().split()))
divisible_by_2 = a[0] % 2
for i in range(1, n):
    if divisible_by_2  != a[i] % 2:
        a.sort()
        break
print(*a)
