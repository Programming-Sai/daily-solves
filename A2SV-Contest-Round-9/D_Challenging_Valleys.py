'''
split the array by the mid point and make sure that the left endpoint is not increasing while the right midpoint is descreasing at the same time
that can only happen to one at a time. if both are at the same time then return NO.
'''



# def check(n, a):
#     l, r = 0, n-1
#     sorted_a = sorted(a)
#     if a == sorted_a or a == sorted_a[::-1]:
#         return 'YES'

#     while l < r:
#         if a[l] < a[l+1]  or a[r-1] > a[r]:
#             return 'NO'
#         l += 1
#         r -= 1
#     return 'YES'

# def check(n, a):
#     bottom = min(a)
#     bottoms = []
#     l = r = 0
#     valleys = 0
#     while r < n-1:
#         while a[r] == bottom:
#             bottoms.append(r)
#             print(l, rr)
#             r += 1
#         l = r 
#         l += 1
#     print(*bottoms)
    
            




def check(n, a):
    seq = []
    valley_point = min(a)
    # l 
    l = r = 0
    while r + 1 < n:
        intermediate = []
        print(l, r)
        while (l == 0 or (a[l - 1] > a[l] and l - 1 > 0) and a[l] == valley_point) and (r == (n-1) or a[r] < a[r + 1] and a[r] == valley_point):
            print(l, r, a[r])
            intermediate.append(a[r])
            r += 1
        # else:
        # l += 1
        r += 1
        l = r
        if intermediate:
            seq.append(intermediate)
    return seq


def check(n, a):
    peak = max(a)
    if a[0] == peak or a[n-1] == peak:
        return 'YES'
    return 'NO'
    


    

def check(n, a):
    new_arr = []
    for x in a:
        if new_arr and x == new_arr[-1]:
            continue
        new_arr.append(x)

    if len(new_arr) <= 2:
        return 'YES'
    
    valley_count = 0
    for i in range(len(new_arr)):
        if i == 0 and  new_arr[i] < new_arr[i+1] :
            valley_count += 1
            continue
            
        elif i == len(new_arr) -1 and  new_arr[i] < new_arr[i-1]:
            valley_count += 1
            continue

        if new_arr[i -1] > new_arr[i] and new_arr[i] < new_arr[i+1]:
            valley_count += 1

    if valley_count == 1:
        return 'YES'
    else:
        return 'NO'

# n = 5
# a = [4, 2, 2, 2, 5]

# n = 7
# a=[3, 2, 2, 1, 2, 2, 3]

n = 11
a = [1, 1, 1, 2, 3, 3, 4, 5, 6, 6, 6]


# n=1
# a=[1000000000]

# print(check(n, a))




t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(check(n, a))