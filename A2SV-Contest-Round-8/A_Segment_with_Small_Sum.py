from fprintx import printx





def check(n, s, a):
    l = r = 0
    max_length = 0
    current_sum = 0
    while r < n:
        current_sum += a[r]
        while current_sum > s:
            current_sum -= a[l]
            l += 1
        max_length = max(max_length, (r - l) + 1)
        r += 1
    
    return max_length


n, s = list(map(int, input().split()))
a = list(map(int, input().split()))
print(check(n, s, a))