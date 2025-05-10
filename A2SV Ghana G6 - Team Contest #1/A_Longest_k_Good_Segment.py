from fprintx import printx

from collections import defaultdict

def check(n, k, a):
    window_set = set()
    index_result = defaultdict(list)
    freq = defaultdict(int)
    l = r = length = 0

    while r < n:
        window_set.add(a[r])
        freq[a[r]] += 1
        while len(window_set) > k:
            freq[a[l]] -= 1
            # print(a[l])
            if freq[a[l]] == 0:
                window_set.remove(a[l])
                del freq[a[l]]
            l += 1
        length = max(length, r-l+1)
        index_result[r-l+1] = (l+1, r+1)
        # printx(length, r-l+1, l, r, window_set, freq, index_result, widths=[10])
        r += 1
    return index_result[length]


# n, k = [9, 3]
# a = [6, 5, 1, 2, 3, 2, 1, 4, 5]
# print(*check(n, k, a))

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(*check(n, k, a))