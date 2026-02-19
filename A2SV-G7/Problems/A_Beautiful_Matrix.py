matrix=[]
range_=5
center = (2, 2)
for _ in range(range_):
    matrix.append(list(map(int, input().split())))

for r in range(range_):
    for c in range(range_):
        if matrix[r][c] == 1:
            print(abs(r-center[0]) + abs(c-center[1]))
            break