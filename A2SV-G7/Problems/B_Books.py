n, t = map(int, input().split())
a = list(map(int, input().split()))
l, r, max_len, window_sum = 0, 0, 0, 0

while r < n:
    window_sum += a[r]
    while window_sum > t:
        window_sum -= a[l]
        l += 1
    max_len = max(max_len, (r-l+1))
    r += 1
print(max_len)