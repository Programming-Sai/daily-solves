from fprintx import printx

# Sliding windows max sum of zeros.


def check(n, k, a, t):
    current_awake_sum = result = current_sum = 0
    for i in range(n):
        if t[i]:
            current_awake_sum += a[i]
    l = r = 0
    while r < n:
        # printx(l, r, a[l], a[r], t[l], t[r], current_awake_sum, current_awake_sum, result, widths=[2])
        if not t[r]: current_sum += a[r]
        if (r-l+1) == k:
            result = max(result, current_awake_sum+current_sum)
            if not t[l]: current_sum -= a[l]
            l += 1
        r += 1
        # if r < n: printx(l, r, a[l], a[r], t[l], t[r], current_awake_sum, current_sum, current_awake_sum+current_sum, result, widths=[2])
    return result

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
t = list(map(int, input().split()))
print(check(n, k, a, t))
