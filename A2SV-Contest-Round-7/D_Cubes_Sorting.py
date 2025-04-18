from fprintx import printx


def check(n, a):
    for i in range(n-1):
        if a[i] <= a[i + 1]:
            print("YES")
            return 
    print("NO")


t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    check(n, a)


    
n=5
a=[5, 3, 2, 1, 4]
# check(n, a)



