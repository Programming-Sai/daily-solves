from collections import Counter

def isSubset(a, b):
    a_count=Counter(a)
    b_count=Counter(b)
    for k in b_count:
        if b_count[k] > a_count[k]:
            return False
    return True


n1=int(input())
a=list(map(int, input().split()))
n2=int(input())
b=list(map(int, input().split()))

print(isSubset(a, b))