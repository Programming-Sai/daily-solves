from fprintx import printx


def check(n,a):
    result = []
    l, r = 0, n-1
    while l <= r:
        result.extend([a[l], a[r]])
        l += 1
        r -= 1
    print(*result[:-1 if n % 2 != 0 else n] )



t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    check(n, a)
    

    
n=7
a = [3, 4, 5, 2, 9, 1, 1]
# check(n, a)
