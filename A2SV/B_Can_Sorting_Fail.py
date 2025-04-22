
def divide_sort_and_check(a, len):
    preffix = a[:len]
    suffix = a[len:]
    preffix.sort()
    suffix.sort()
    d = preffix + suffix
    if is_sorted(d):
        return 'NO'
    else:
        return 'YES'



def is_sorted(a):
    for i in range(len(a[1:])):
        if a[i] > a[i+1]:
            return False
    return True

# a=[3, 1, 2, 1]
# a=[1,2,2,4,4]
# a=[2,2,1]
# n=len(a)
# s={divide_sort_and_check(a, i) for i in range(n)}
# if len(s) == 1:
#     print('NO')
# else:
#     print('YES')


# print(divide_sort_and_check(a, 3))
# print(is_sorted(a))
# print(is_sorted([1,2,3,4]))


t=int(input())
for _ in range(t):
    n=int(input())
    a=map(int, input().split())
    a=list(a)
    s={divide_sort_and_check(a, i) for i in range(n)}
    if len(s) == 1:
        print('NO')
    else:
        print('YES')







# It is guaranteed that the sum of n over all test cases does not exceed 104.