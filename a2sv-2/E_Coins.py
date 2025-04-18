
def check(n, k):
    if n % 2 != 0 and k % 2 == 0:
        print("NO")
    else:
        print("YES")



t=int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    check(n, k)
    