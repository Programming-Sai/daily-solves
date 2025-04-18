def check(p):
    max_point=p[0]
    min_point=p[0]
    res = 0
    for i in range(1, len(p)):
        if p[i] > max_point:
            res+=1
            max_point = p[i]
        elif p[i] < min_point:
            res+=1
            min_point = p[i]
    return res


n=int(input())
points = list(map(int, input().split()))
print(check(points))

