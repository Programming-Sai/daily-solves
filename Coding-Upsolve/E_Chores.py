def check(n, k, x, a):
    min_time = 0
    temp_k = k
    for i in range(n-1, -1, -1):
        if temp_k > 0:
            min_time += x
            temp_k -= 1
            continue
        min_time += a[i]
    print(min_time)


n, k, x = list(map(int, input().split()))
a=list(map(int, input().split()))
check(n, k, x, a)




# n=4
# k=2
# x=2
# a=[3, 6, 7, 10]

# n=5
# k=2
# x=1
# a=[100, 100, 100, 100, 100]
# check(n, k, x, a)

