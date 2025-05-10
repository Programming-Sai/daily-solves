from fprintx import printx

def check(n, t):
    if n == 2:
        return 1,1
    l = ta = tb = a = b =  0
    r = n-1


    ta += t[l]
    tb += t[r]
    l += 1
    a += 1
    r -= 1
    b += 1

    while l <= r:
        if ta > tb:
            tb += t[r]
            b += 1
            r -= 1
        else:
            ta += t[l]
            a += 1
            l += 1
    
    if ta > tb:
        b += 1
    else:
        a += 1

    return a, b



n = int(input())
t = list(map(int, input().split()))
print(*check(n, t))