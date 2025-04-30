def counter(s, x, y):
    l, r = x-1, y
    a=s[l:r]
    count = 0
    for i in range(len(a)):
        if (i+1) < len(a):
            if a[i] == a[i+1]:
                count += 1
    print(count)
 



def counter_prefix(s, l, r):
    prefix_sum = [0] * len(s)
    for i in range(1, len(s)):
        prefix_sum[i] = prefix_sum[i-1] + (s[i] == s[i-1])
    print(prefix_sum[r-1] - prefix_sum[l-1], prefix_sum , prefix_sum[r-1], prefix_sum[l-1], r-1, l-1)   


counter_prefix("#..###", 1, 3)
counter_prefix("#..###", 5, 6)
counter_prefix("#..###", 1, 5)
counter_prefix("#..###", 3, 6)
counter_prefix("#..###", 3, 4)


# s=input()
# prefix_sum = [0] * len(s)
# for i in range(1, len(s)):
#     prefix_sum[i] = prefix_sum[i-1] + (1 if s[i] == s[i-1] else 0)

# m=int(input())
# for _ in range(m):
#     l, r = list(map(int, input().split()))
#     # counter(s, l, r)
#     print(prefix_sum[r-1] - prefix_sum[l-1])    