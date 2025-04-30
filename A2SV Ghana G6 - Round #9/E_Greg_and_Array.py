from itertools import accumulate
from fprintx import printx


def check(n, m, k, a, ops, queries):
    query_ops_count = [0] * (m+1)
    for x, y in queries:
        query_ops_count[x-1] += 1
        query_ops_count[y] += -1
    
    for i in range(1, m+1):
        query_ops_count[i] += query_ops_count[i-1]

    # query_ops_count = list(accumulate(query_ops_count))
    a_count = [0] * (n+1)

    for i in range(m):
        a_count[ops[i][0]-1] += (ops[i][2] * query_ops_count[i])
        a_count[ops[i][1]] += -(ops[i][2] * query_ops_count[i])
        # printx(a_count, ops[i][0]-1, ops[i][1], (ops[i][2] * query_ops_count[i]), widths=[30])
    # a_count = list(accumulate(a_count))
    for i in range(1, n+1):
        a_count[i] += a_count[i-1]
    # print(query_ops_count, a, list(accumulate(a_count)))
    for i in range(n):
        # printx(a[i], a_count[i])
        a[i] += a_count[i]
    return a

        


n, m, k = [3, 3, 3]
a = [1, 2, 3]

ops = [
    [1, 2, 1], 
    [1, 3, 2], 
    [2, 3, 4]
    ]

queries = [[1, 2], [1, 3], [2, 3]]
# print(*check(n, m, k, a, ops, queries))


n, m, k = list(map(int, input().split()))
a = list(map(int, input().split()))
ops = [list(map(int, input().split())) for _ in range(m)]
queries = [list(map(int, input().split())) for _ in range(k)]
print(*check(n, m, k, a, ops, queries))