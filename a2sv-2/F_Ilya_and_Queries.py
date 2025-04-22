
# s="#..###"
# l, r = 3-1, 4

def counter(s, x, y):
    l, r = x-1, y
    a=s[l:r]
    count = 0
    for i in range(len(a)):
        if (i+1) < len(a):
            if a[i] == a[i+1]:
                count += 1
    print(count)

s=input()
m=int(input())
for _ in range(m):
    l, r = list(map(int, input().split()))
    counter(s, l, r)