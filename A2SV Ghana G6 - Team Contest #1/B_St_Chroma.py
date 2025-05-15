from fprintx import printx



def check(n, x):
    if n == 1:
        return [0]
    result = []
    for i in range(1, n):
        if i <= x:
            result.append(x-i)
        else:
            result.append(x+(i-x))
    if x < n:
        result.append(x)
    else:
        result.append(0)
    return result

# n, x = 4, 4
# print(*check(n, x)) 


t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    print(*check(n, x))