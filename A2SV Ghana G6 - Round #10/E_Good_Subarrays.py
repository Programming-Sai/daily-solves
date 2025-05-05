from fprintx import printx



from itertools import accumulate
from collections import defaultdict


def check(n, a):
    sum_hash = defaultdict(int)
    sum_hash[0] = 1
    # prefix_sum = list(accumulate(a))
    curr_sum = 0
    result_count = 0
    for r in range(n):
        curr_sum = a[r]
        # if curr_sum == (r-l+1):
            # printx(curr_sum)
        result_count += sum_hash[curr_sum - 6]
            # l += 1

        sum_hash[curr_sum] += 1
        # r += 1

    return result_count

    # result_sum = 0
    # curr_sum = 0
    # for r in range(n):
    #     curr_sum += a[r]

    #     if a[r] == 1:
    #         result_sum += 1

    #     if curr_sum == (r+1):
    #         print(a[:r], r)
    #         result_sum += 1

    # curr_sum = 0
    # for l in range(n-1, -1, -1):
    #     curr_sum +=  a[l]
    #     if curr_sum == l + 1:
    #         # print(l, "-")
    #         print(a[l:], l)
    #         result_sum += 1
    
    # return result_sum


# n = 3
# a = [1, 2, 0]
# n = 5
# a = [1, 1, 0, 1, 1]
n = 6
a = [6, 0, 0, 0, 0, 5]
print(check(n, a))


# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input()))
#     print(check(n, a))