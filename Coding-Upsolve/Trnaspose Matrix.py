from fprintx import printx


def transpose(matrix):
            # return [[matrix[c][r] for c in range(len(matrix) -1, -1, -1)] for r in range(len(matrix[0]))] # For Rotating 90 deg
            return [[matrix[c][r] for c in range(len(matrix))] for r in range(len(matrix[0]))] # For Transposing


# print(transpose(matrix = [[1,2,3],[4,5,6]]))
print(transpose([[1,2,3],[4,5,6],[7,8,9]]))
# print(transpose(matrix = [[1,2,3],[4,5,6],[7,8,9]]))

'''
[
    [1,4],
    [2,5],
    [3,6]
]

'''