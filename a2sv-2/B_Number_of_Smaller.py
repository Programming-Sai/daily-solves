from fprintx import printx

def check(n, m, a, b):
    c = []
    l = 0

    for num in b:
        while  l < n and a[l] < num:
            # printx(l, a[l], num, c, widths=[4])
            l += 1 
        c.append(l)
    print(*c)




n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
check(n, m, a, b)