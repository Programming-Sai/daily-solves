from fprintx import printx


import math

def canRead(n, a, t, mid):
    l = r = s_count = 0
    while r < n:
        while s_count > t:
            s_count -= a[l]
            l += 1
        s_count += a[r]
        # printx(s_count, t, r-l+1, mid)
        if s_count <= t and (r-l+1) == mid:
            return True
        r += 1
    return False
        

def check(n, t, a):
    l, r = 0, n
    ans = -1
    while l <= r:
        # mid = l + (r-l)//2
        mid = math.ceil((l+r)/2)
        # print(mid, l, r, (r-l)//2)
        if canRead(n, a, t, mid):
            ans = mid
            l = mid+1
        else:
            r = mid - 1
    return ans if ans > -1 else l



n, t = map(int, input().split())
a = list(map(int, input().split()))
print(check(n, t, a))
# print(canRead(n, a, t, 3))