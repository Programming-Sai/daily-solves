from fprintx import printx


def check(n, a):
    result = 0
    operation_count = 0
    l = r = 0

    # while r < n:
    # # for l in range(n):
    #     if a[l] > 0:
    #         operation_count += 1
    #     if a[l] < 0:
    #         result += -(a[l])
    #     else:
    #         result += a[l]
    #     l += 1
    #     r += 1

    while r+1 < n:
        printx(1, r)
        if a[r] > 0:
            l = r + 1
        r += 1
        

    print(*[result, operation_count])


def check(n, a):
    running_sum = r = count = 0
    for x in a:
        running_sum += (x if x >= 0 else -x)

    while r < n:
        met_neg = False
        while r < n and a[r] <= 0:
            # printx(r, a[r])
            met_neg = met_neg or (a[r] < 0)
            r += 1
        count += met_neg
        r += 1
    return (running_sum, count)



# n = 6
# a = [-1, 7, -4, -2, 5, -8]
# print(check(n, a))


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(*check(n, a))
