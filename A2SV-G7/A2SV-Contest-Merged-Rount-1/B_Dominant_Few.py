
t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))
    k = 1
    e_sum = 0
    c_sum = a[0]
    while ((2*k) + 1) <= n:
        e_sum += a[-k]
        c_sum += a[k]
        if e_sum > c_sum:
            print("YES")
            break
        k += 1
    else:
        print("NO")
