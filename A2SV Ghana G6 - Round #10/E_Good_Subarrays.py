from fprintx import printx

from collections import defaultdict


def check(n, a):
    sum_hash = defaultdict(int)
    curr_sum = 0
    result_count = 0
    l = r = 0
    while r < n:
        curr_sum += a[r]
        if curr_sum == (r-l+1):
            # printx(curr_sum)
            result_count += sum_hash[curr_sum]
            l += 1

        sum_hash[curr_sum] += 1
        r += 1
        printx(sum_hash, l, r, curr_sum, a[l:r], widths=[15])

    return result_count


n = 3
a = [1, 2, 0]
print(check(n, a))


# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input()))
#     print(check(n, a))