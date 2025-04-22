from fprintx import printx


def check(n, a):
    if n == 1 or len(set(a)) == 1:
        print(0)
        return
    a.sort()
    # print(a)
    l = 0
    r = n-1
    result  = 0
    while l < r:
        # printx(result, a[r],  a[l], a[r-1], a[l+1],)
        result += a[r] - a[l]
        l += 1
        r -= 1
    print(result)



t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    check(n, a)




n =5
a =[1, 5, 6, 3, 4]

n = 6
a=[1, 13, 9, 3, 7, 2]
# check(n, a)
