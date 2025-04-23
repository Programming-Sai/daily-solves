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



n = 6
a = [-1, 7, -4, -2, 5, -8]
check(n, a)



# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     check(n, a)
