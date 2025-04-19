'''
split the array by the mid point and make sure that the left endpoint is not increasing while the right midpoint is descreasing at the same time
that can only happen to one ata a time. if both are at the same time then return NO.
'''



def check(n, a):
    l, r = 0, n-1
    sorted_a = sorted(a)
    if a == sorted_a or a == sorted_a[::-1]:
        return 'YES'

    while l < r:
        if a[l] < a[l+1]  or a[r-1] > a[r]:
            return 'NO'
        l += 1
        r -= 1
    return 'YES'




t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(check(n, a))