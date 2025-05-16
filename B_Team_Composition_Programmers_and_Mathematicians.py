from fprintx import printx

def check(a, b):
    l = ans = 0
    r = min(a, b)
    while l <= r:
        mid = l + (r-l)//2
        if (a >= mid and b >= mid and (mid*4) <= (a+b)):
            ans = mid
            l = mid+1
        else:
           r = mid-1

    return ans



t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(check(a, b))


# print(1000000000 == 1000000000, 3+(6-3)//2)
# print(check(6, 6))