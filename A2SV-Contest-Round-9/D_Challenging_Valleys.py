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
    

n = 5
a = [4, 2, 2, 2, 5]

# n = 7
# a=[3, 2, 2, 1, 2, 2, 3]
print(check(n, a))




# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     print(check(n, a))