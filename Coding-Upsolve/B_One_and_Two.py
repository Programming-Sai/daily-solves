import math


def check(a):
    total_product = math.prod(a)
    product_up_to_i = 1
    for i in range(len(a) - 1):        
        product_up_to_i *= a[i]
        if (product_up_to_i) == (total_product // product_up_to_i):
            return i + 1
    
    return -1




t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    print(check(a))

