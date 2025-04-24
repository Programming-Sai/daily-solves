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
    l = r = i = count = 0

    while r < n:
        printx(l, r, a[l:r+1], a[i], i, widths=[15])
        while a[r] > 0:
            count += 1
            l = r+1
            r += 1
        r += 1

        i += 1
    print()
    return count
    



n = 6
a = [-1, 7, -4, -2, 5, -8]
# print(check(n, a))

print(1 << 2)



# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     print(check(n, a))
