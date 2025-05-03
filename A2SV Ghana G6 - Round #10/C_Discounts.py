from fprintx import printx

from itertools import accumulate

def check(n, a, m, q):
    a.sort(reverse=True)
    prefix_sum = list(accumulate(a))
    # printx(sum(a[:2]), a, prefix_sum, prefix_sum[1], prefix_sum[-1] - prefix_sum[2], widths=[3])

    for que in q:
        print(prefix_sum[que-2] + prefix_sum[-1] - prefix_sum[que-1])

n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))
(check(n, a, m, q))