
from fprintx import printx

def print_matrix(matrix):
    for i in range(len(matrix)):
        row = ""
        for j in range(len(matrix[i])):
            row += f" {matrix[i][j]} "
        print(row)


def remove_duplicates(i, j, matrix, col, already_seen, n, m):
    row = [x for x in matrix[i]]
    col = col[j]
    # print(row, col)

    for r in range(len(row)):
        if row[r] == matrix[i][j] and (i, j) not in already_seen and r != j:
            already_seen.add((i, j))
            # printx(r, j, row[r], matrix[i][j], (i, j), "Row", already_seen, widths=[5])

    for c in range(len(col)):
        if col[c] == matrix[i][j] and (i, j) not in already_seen and c != i:
            already_seen.add((i, j))
            # printx(c, i, col[c], matrix[i][j], (i, j), "Col", already_seen, widths=[5])

    


def check(r, c, matrix):
    already_seen = set()
    # Loop Through all items and keep track of those already visited to avoid wasting time
    row_len = len(matrix)
    col_len = len(matrix[0])
    column = [[matrix[y][x] for y in range(row_len)] for x in range(col_len)]

    for row in range(row_len):
        for col in range(col_len):
            if (row, col) in already_seen:
                continue
            remove_duplicates(row, col, matrix, column, already_seen, row_len, col_len)
    for row in range(row_len):
        for col in range(col_len):
            if (row, col) in already_seen:
                continue
            print(matrix[row][col], end='')
    print()


r, c = list(map(int, input().split()))
matrix = [input() for _ in range(r)]
check(r, c, matrix)


r, c = 5, 5
[[1,2,3],[4,5,6],[7,8,9]]

matrix = [
        'fcofd', 
        'ooedo', 
        'afaoa', 
        'rdcdf', 
        'eofsf'
]

# r, c = 3, 3
# matrix = [
#             'cba', 
#             'bcd', 
#             'cbc'
#         ]



# check(r, c, matrix)

