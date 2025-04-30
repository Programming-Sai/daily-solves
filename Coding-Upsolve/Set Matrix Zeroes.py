from fprintx import printx


def setZeroe(matrix):
    already_seen = set()

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if (r, c) not in already_seen and matrix[r][c] == 0:
                for k in range(len(matrix[r])):
                    if (matrix[r][k] == 0  and (r, k) != (r, c)):
                        continue
                    
                    printx(r, k, r, c, "Row-Setting", already_seen, widths=[10])
                    matrix[r][k] = 0
                    already_seen.add((r, k))

                for k in range(len(matrix[r])):
                    if k >= len(matrix) or (matrix[k][r] == 0  and (k, r) != (r, c)):
                        continue

                    printx(r, k, r, c, "Col-Setting", already_seen, widths=[10])
                    matrix[k][r] = 0
                    already_seen.add((k, r))

def setZeroes(matrix):
    already_zero_row = set()
    already_zero_col = set()

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 0:
                already_zero_col.add(c)
                already_zero_row.add(r)

    print(already_zero_row, already_zero_col)

    # Setting Rows
    for r in already_zero_row:
        matrix[r] = [0] * len(matrix[r])

    # Setting Cols
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if c in already_zero_col:
                matrix[r][c] = 0




def print_matrix(matrix):
    for i in range(len(matrix)):
        row = ""
        for j in range(len(matrix[i])):
            row += f" {matrix[i][j]} "
        print(row)
    



matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)
print()
print(matrix)
print_matrix(matrix)