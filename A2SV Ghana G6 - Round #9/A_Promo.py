from fprintx import printx


def check(n, p, queries):
    p.sort(reverse=True)
    prefix_sum = [0]*(n+1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + p[i]
    # print(prefix_sum)

    for x, y in queries:
        # print(sum(p[:x][x-y:]))
        print(prefix_sum[x] - prefix_sum[x-y])
    # return result

n, q = list(map(int, input().split()))
p = list(map(int, input().split()))
queries = []
for _ in range(q):
    queries.append(list(map(int, input().split())))
(check(n, p, queries))