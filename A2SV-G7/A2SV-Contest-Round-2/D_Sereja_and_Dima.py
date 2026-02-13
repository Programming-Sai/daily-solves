n=int(input())
s=list(map(int, input().split()))

c_p, s_s, d_s, l, r = 0, 0, 0, 0, n-1
while l <= r:
    if s[l] > s[r]:
        c_m = s[l]
        l += 1
    else:
        c_m = s[r]
        r -= 1
    if c_p:
        d_s += c_m
    else:
        s_s += c_m
    c_p = 1 - c_p

print(s_s, d_s)