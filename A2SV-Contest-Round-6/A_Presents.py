

n=int(input())
p=list(map(int, input().split()))
output = [0] * (n)
for i in range(n):
    output[p[i] - 1] = i + 1
for i in output: 
    print(i, end=' ')

