def check(m):
    result = [[1] * 3 for _ in range(3)]  
    for i in range(3):
        for j in range(3):
            if m[i][j] % 2 == 1:  
                toggle_adjacents(i, j, result)
    print_matrix(result)


def toggle_adjacents(i, j, m):
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    m[i][j] = 1 - m[i][j]
    for x, y in offsets:
        new_i = i + x
        new_j = j + y
        if 0 <= new_i <= 2 and 0 <= new_j <= 2:
            m[new_i][new_j] = 1 - m[new_i][new_j]


def print_matrix(m):
    for i in m:
        for j in i:
            print(j, end="")
        print()


m = []
for i in range(3):
    m.append(list(map(int, input().split())))
check(m)



# m = [
#     [1,0,0],
#     [0,0,0],
#     [0,0,1]
# ]

# m=[
#     [1,0,1],
#     [8,8,8],
#     [2,0,3]
# ]




# check(m)



# toggle_adjacents(2, 0, m)



