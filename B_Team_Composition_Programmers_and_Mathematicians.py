from fprintx import printx

def check(a, b):
    min_cat = min(a, b)
    if (a == 0 or b == 0):
        return 0
    if (a < 4 and b < 4):
        return 1
    if min_cat < 4:
        return min_cat
    
    l = 0
    r = min_cat
    while l < r:
        mid = l + (r-l)//2
        if ((mid*4) > (a+b)):
            r = mid-1
        else:
            l = mid

    return l



# t = int(input())
# for _ in range(t):
#     a, b = map(int, input().split())
#     print(check(a, b))


print(1000000000 == 1000000000, 3+(6-3)//2)
print(check(6, 6))