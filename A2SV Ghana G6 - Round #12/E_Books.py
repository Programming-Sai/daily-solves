from fprintx import printx



def canRead(n, a, t, mid):
    l = r = s_count = 0
    while r < n:
        while s_count > t:
            s_count -= a[l]
            l += 1
        s_count += a[r]
        r += 1

    if s_count <= t:
            return True
    return False
        

def check(n, t, a):
    pass



n, t = map(int, input().split())
a = list(map(int, input().split()))
# print(check(n, t, a))
print(canRead(n, a, t, 1))