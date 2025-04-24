from fprintx import printx


def equalSubstring(s, t, maxCost):
    n = len(s)
    l = r = current_cost = max_length = 0
    while r < n:
        # printx(l, r, current_cost, abs(ord(s[r]) - ord(t[r])), max_length, (r-l+1), s[l:r+1], widths=[3])
        current_cost += abs(ord(s[r]) - ord(t[r]))
        while current_cost > maxCost:
            current_cost -= abs(ord(s[l]) - ord(t[l]))
            l += 1
        if (r-l+1) > max_length:
            max_length = (r-l+1)
        # max_length = max(max_length, (r-l+1))
        r += 1
    return max_length




print(equalSubstring(s = "abcd", t = "bcdf", maxCost = 3)) # 3
print(equalSubstring(s = "abcd", t = "cdef", maxCost = 3)) # 1
print(equalSubstring(s = "abcd", t = "acde", maxCost = 0)) # 1