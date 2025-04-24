from fprintx import printx


class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix
        m = len(matrix)
        n = len(matrix[0])
        print(m, n)
        self.prefix_sum = [[0] * (n+1) for i in range(m+1)]
        # [[0] * (len(matrix[0])+1) for i in range(len(matrix)+1)]
        for r in range(1, m+1):
            for c in range(1, n+1):
                self.prefix_sum[r][c] = (matrix[r-1][c-1] + self.prefix_sum[r][c-1] + self.prefix_sum[r-1][c]) - (self.prefix_sum[r-1][c-1])
        print_matrix(self.prefix_sum)



    def sumRegion(self, row1, col1, row2, col2):
        return (self.prefix_sum[row2+1][col2+1] - self.prefix_sum[row2+1][col1] - self.prefix_sum[row1][col2+1]) + self.prefix_sum[row1][col1]


def print_matrix(matrix):
    for i in matrix[1:]:
        printx(*i[1:], widths=[3], alignments=['^']) 


inputs = [
    [[
        [3, 0, 1, 4, 2], 
        [5, 6, 3, 2, 1], 
        [1, 2, 0, 1, 5], 
        [4, 1, 0, 1, 7], 
        [1, 0, 3, 0, 5]

    ]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]


x = NumMatrix(inputs[0][0])

# print(x)
for i in range(1, len(inputs)):
    print(x.sumRegion(*inputs[i]))
