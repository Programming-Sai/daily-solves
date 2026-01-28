t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))
    
    for i in range(5):
        min_value = min(l)
        min_idx = l.index(min_value)
        l[min_idx] += 1

    a, b, c = l
    print(a*b*c)
