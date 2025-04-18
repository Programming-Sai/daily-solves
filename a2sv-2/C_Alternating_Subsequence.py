from fprintx import printx


def check(n, a):
    # Get the sequences
    starts = []
    ends = []
    maxes = []
    l = r = 0
    count = 0
    length = 0
    max_length = 0
    max_count = float('-inf')
    while r < n:
        if is_alternating(a[r], a[min(r+1, n - 1)]):
            # print('-------Start')
            l = r
            count += a[l]
            starts.append(l)
        else:
            if starts and r-1 == starts[-1]:
                count += a[r]
                starts.append(r)
                length = (starts[-1] - starts[0]) + 1
                maxes.append((length, count))
                max_length = max(length, max_length)
                max_count = max(count, max_count)
                printx(is_alternating(a[r], a[min(r+1, n - 1)]), l, r, r+1, n, max_length, max_count, starts, maxes, length, count, a[l], a[r], a[min(r+1, n - 1)], widths=[9])
                starts.clear()
                length = 0
                count = 0
        r += 1

    if max_count == float('-inf'):
        return a[0]
    result_count = float('-inf')
    for length, count in maxes:
        if length == max_length:
            result_count = max(count, result_count)

    return result_count


def is_alternating(i, j):
    return (i/abs(i)) != (j/abs(j)) 


def check(n, a):
    a.append(-(a[-1]))
    result_count = 0
    max_item = float('-inf')
    for i in range(n):
        max_item = max(max_item, a[i])
        if is_alternating(a[i], a[i+1]):
            # printx(i, max_item, result_count, a[i], a, 'Before', widths=[5])
            result_count += max_item
            max_item = float('-inf')
            # printx(i, max_item, result_count, a[i], a, 'After', widths=[5])
    return result_count



t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(check(n, a))




n=5
a=[1, 2, 3, -1, -2]
# n = 13
# a=([1, 2, 3, -1, 2, -10, 4, -3, 2, -11, 5, 1, 5])
n=10
a = [-2, 8, 3, 8, -4, -15, 5, -2, -3, 1]

# n=11
# a = [-2, 8, -1, -3, 8, -4, -15, 5, -2, -3, 10]
# n=4
# a=[-1, -2, -1, -3]
# a=[1, 2, 3, 4]
# print(check(n, a))
