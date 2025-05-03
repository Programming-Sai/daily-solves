from fprintx import printx

from itertools import accumulate

def check(n, v, m, q):
    sorted_stones = sorted(v)
    # print(sorted_stones)

    prefix_sum_normal = list(accumulate(v))
    prefix_sum_sorted = list(accumulate(sorted_stones))
    types = [
        prefix_sum_normal,
        prefix_sum_sorted
    ]

    for type_, l, r in q:
        arr = types[type_ - 1]
        # printx(arr, arr[r-1], arr[l-2])
        if l > 1:
            print(arr[r-1] - arr[l-2])
        else:
            print(arr[r-1])
    



n = int(input())
v = list(map(int, input().split()))
m = int(input())
q = []
for _ in range(m):
    q.append(list(map(int, input().split())))
check(n, v, m, q)