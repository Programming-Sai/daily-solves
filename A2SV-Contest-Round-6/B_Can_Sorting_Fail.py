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
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return False
    return True
    
    
 
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    # if is_sorted(a):

    # s={divide_sort_and_check(a, i) for i in range(n)}
    if is_sorted(a):
        print('NO')
    else:
        print('YES')
 
    