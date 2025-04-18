
def check(n, a):
    i = j = 0
    for x in range(n):
        if a[x] < a[i]:
            i = x
        elif a[x] > a[j]:
            j = x
    print(i+1, j+1)


t=int(input())
for _ in range(t):
    n=int(input())
    a = list(map(int, input().split()))
    check(n, a)