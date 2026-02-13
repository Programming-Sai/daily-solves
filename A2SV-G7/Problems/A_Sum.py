t = int(input())
for _ in range(t):
    a, b, c = sorted(map(int, input().split()))
    # print(a, b, c, a+b)
    if (a + b) == c:
        print("YES")
    else:
        print("NO")
