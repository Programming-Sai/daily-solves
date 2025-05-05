from fprintx import printx



from itertools import accumulate
from collections import defaultdict


def check(n, a):
    counter = defaultdict(int)
    counter[0] = 1
    prefix_sum = 0
    result_count = 0
    ad = 0
    for i in range(n):
        # printx(counter, ad, counter[ad], prefix_sum, i+1, result_count, "Before", widths=[5])
        prefix_sum += a[i]
        ad = prefix_sum - (i+1)
        result_count += counter[ad]
        counter[ad] += 1
        # printx(counter, ad, counter[ad], prefix_sum, i+1, result_count, "After\n\n", widths=[5])
    return result_count
    



# n = 3
# a = [1, 2, 0]
# n = 5
# a = [1, 1, 0, 1, 1]
# n = 6
# a = [6, 0, 0, 0, 0, 5]
# print(check(n, a))


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input()))
    print(check(n, a))