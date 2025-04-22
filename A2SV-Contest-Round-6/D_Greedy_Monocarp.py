
# def check(n, k, a):
#     print(a)
#     # First find the prefix sum
    # prefix_sum = [0] * n
    # for i in range(n):
    #     prefix_sum[i] = a[i] + prefix_sum[i-1]
#     print(prefix_sum)

#     # find the min
#     min_res = float('inf')
#     for i in range(n):
#         # if k - prefix_sum[i] < 0:
#             # print(min_res)
#             # print(k - prefix_sum[i], min_res, "lk")
#             # return
#         print(k, prefix_sum[i], k - prefix_sum[i])
#         min_res = min(min_res, (k - prefix_sum[i]))
        
#     print(min_res)




from fprintx import printx


def check(n, k, a):
    a = sorted(a, reverse=True)
    current_have = a[0]
    prev_have = 0
    for i in range(1,n):
        current_have += a[i]
        prev_have += a[ i-1]        
        # printx(a, current_have, prev_have, i, a[i], k, k-prev_have)

        if current_have >= k:
            print(k - prev_have)
            return
    print(k-current_have)



def check2(n, k, a):
    a=sorted(a, reverse=True)
    total = 0
    for i in range(n):
        if total + a[i] == k:
            return 0
        elif total + a[i] > k:
            return k - total
        else:
            total += a[i]

    return k-total


# n, k, a = 5, 4, [4, 1, 2, 3, 2]
# n, k, a = 5, 10, [4, 1, 2, 3, 2]

# [4, 3, 2, 2, 1]
# n, k, a = 2, 10, [1, 1]
# n, k, a = 3, 8, [3, 3, 3]
# check(n, k, a)

t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print(check2(n, k, a))



# TODO
# Sort a
# have 2 wars, curr_have and prev_have
# curr_have = prefix_sum[i] and prev_have = prefix_sum[i-1]
# return k - prev_have only when curr_have >- k
