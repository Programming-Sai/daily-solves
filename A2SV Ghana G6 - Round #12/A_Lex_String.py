from fprintx import printx


def check(n, m, k, a, b):
    a = sorted(a)
    b = sorted(b)
    c = ""
    # printx(n, m, k, a, b, widths=[3])
    range_n = min(n, m)
    i = op_count = j = 0
    print(a[0] < b[0])
    while True:
        if j > range_n or i > range_n: break
        if op_count >= k: 
            i, j = j, i
            op_count = 0
        printx(i, j, op_count)
        if a[i] < b[j]:
            c += a[i]
            i += 1
        else:
            c += b[j]
            j += 1
        op_count += 1
    return c



n, m, k = 5, 9, 3
a, b = "caaca", "bedededeb"
print(check(n, m, k, a, b))


# t = int(input())
# for _ in range(t):
#     n, m, k = map(int, input().split())
#     a = input()
#     b = input()
#     print(check(n, m, k, a, b))