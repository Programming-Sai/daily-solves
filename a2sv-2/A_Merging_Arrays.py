
from fprintx import printx

def check(n, m, a, b):
    l, r = 0, 0
    # lowest_length = min(n, m)
    c = []

    # if n == lowest_length:
    #     small_pointer = 0
    #     other_pointer = 0
    #     main_arr = b
    #     endpoint = n
    # else:
    #     small_pointer = 0
    #     other_pointer = 0
    #     main_arr = a
    #     endpoint = m

    while l < n and r < m:
        if a[l] < b[r]:
            c.append(a[l])
            l += 1
        else:
            c.append(b[r])
            r += 1
    
    # print(c, small_pointer, other_pointer)
    c.extend(a[l:])
    c.extend(b[r:])
    print(*c)


n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
check(n, m, a, b)



# n, m = 6, 7
# a = [1, 6, 9, 13, 18, 18]
# b= [2, 3, 8, 13, 15, 21, 25]
# check(n, m, a, b)

