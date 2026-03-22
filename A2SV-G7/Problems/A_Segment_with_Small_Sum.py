n, s = map(int, input().split())
a = list(map(int, input().split()))
l, r, max_length, window_sum = 0, 0, float("-inf"), 0
while r < n:
    window_sum += a[r]
    while window_sum > s:
        window_sum -= a[l]
        l += 1
    max_length = max(max_length, r - l + 1)
    r += 1
print(max_length)
