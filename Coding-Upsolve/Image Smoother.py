from fprintx import printx
from math import floor


def imageSmoother(img):
    row_length, col_length = len(img), len(img[0]), 
    return [[get_neighbouring_average(img, r, c, row_length, col_length) for c in range(col_length)] for r in range(row_length)]
    
    # for i in range(row_length):
    #     for j in range(col_length):
    #         average = get_neighbouring_average(img, i, j, row_length, col_length)
    #         output[i][j] = average
            # printx(output, i, j, average, widths=[5])


def get_neighbouring_average(matrix, r, c, m, n):
    total = 0
    number_of_cells = 0
    # +
    if r - 1 >= 0:
        total += matrix[r - 1][c]
        number_of_cells += 1
        # printx(total, number_of_cells, r, c, matrix[r - 1][c], "(r-1 >= 0)", widths=[5])
    if r + 1 < m:
        total += matrix[r + 1][c]
        number_of_cells += 1
        # printx(total, number_of_cells, r, c, matrix[r + 1][c], "(r+1 < m)", widths=[5])
    if c - 1 >= 0:
        total += matrix[r][c - 1]
        number_of_cells += 1
        # printx(total, number_of_cells, r, c, matrix[r][c - 1], "(c-1 >= 0)", widths=[5])
    if c + 1 < n:
        total += matrix[r][c + 1]
        number_of_cells += 1
        # printx(total, number_of_cells, r, c, matrix[r][c + 1], "(c+1 < n)", widths=[5])

    # x
    if r - 1 >= 0 and c - 1 >= 0:
        total += matrix[r - 1][c - 1]
        number_of_cells += 1
        # printx(total, number_of_cells, r, c, matrix[r - 1][c - 1], "(r - 1, c - 1)", widths=[5])
    if r + 1 < m and c - 1 >= 0:
        total += matrix[r + 1][c - 1]
        number_of_cells += 1
        # printx(total, number_of_cells, r, c, matrix[r + 1][c], "(r + 1, c - 1)", widths=[5])
    if r - 1 >= 0 and c + 1 < n:
        total += matrix[r - 1][c + 1]
        number_of_cells += 1
        # printx(total, number_of_cells, r, c, matrix[r][c - 1], "(r - 1, c + 1)", widths=[5])
    if r + 1 < m and c + 1 < n:
        total += matrix[r + 1][c + 1]
        number_of_cells += 1
        # printx(total, number_of_cells, r, c, matrix[r][c + 1], "(r + 1, c + 1)", widths=[5])

    total += matrix[r][c]
    number_of_cells += 1
    # printx(total, number_of_cells, r, c, matrix[r][c], "()", widths=[5])
    
    return floor(total / max(1, number_of_cells))



# print(imageSmoother(img = [[1,1,1],[1,0,1],[1,1,1]]))
print(imageSmoother(img = [[100,200,100],[200,50,200],[100,200,100]]))