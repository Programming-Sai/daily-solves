from fprintx import printx



def check(matrix):
    prefix_sum = [[0] * (len(matrix[0])+1) for i in range(len(matrix)+1)]

    for row in range(1, len(prefix_sum)):
        for col in range(1, len(prefix_sum[row])):
            prefix_sum[row][col] = (matrix[row -1][col-1] + prefix_sum[row-1][col] + prefix_sum[row][col-1]) - prefix_sum[row - 1][col - 1]


    print_matrix(prefix_sum)



def print_matrix(matrix):
    for i in matrix[1:]:
        printx(*i[1:], widths=[3], alignments=['^'])

matrix = [
    [3, 2, 1, 4],
    [6, 7, 11, 9],
    [0, 12, 8, 15],
    [3, -1, 20, -2]
]

(check(matrix))