from fprintx import printx

def check(s, m, queries):
    prefix_sum = [0] * (len(s)+1)
    s_diff = [0 if i+1 < len(s) and s[i] != s[i+1] else 1 for i in range(len(s))]
    for i in range(len(s_diff)):
        prefix_sum[i+1] = prefix_sum[i] + s_diff[i]

    # print(prefix_sum)
    for l, r in queries:
        # print(sum(p[:x][::-1][:y]))
        # printx(prefix_sum[r-1] - prefix_sum[l-1], r, l, r-1, l-1)
        print(prefix_sum[r-1] - prefix_sum[l-1])


s = input()
m = int(input())
queries = []
for _ in range(m):
    queries.append(list(map(int, input().split())))
check(s, m, queries)
