def matrixReshape(mat, r, c):
    m, n = len(mat), len(mat[0])
    if m*n != r*c:
        return mat
    output = [[0 for i in range(c)] for j in range(r)]
    i, j = 0,0
    for row in range(r):
        for col in range(c):
            # print(row, col, i, j, output, m, n)
            output[row][col] = mat[i][j]
            if j + 1 < n:
               j += 1
            else:
                j = 0
                i += 1
    return output


print(matrixReshape(mat = [[1,2],[3,4], [5, 6]], r = 1, c = 6))
print(matrixReshape(mat = [[1,2],[3,4]], r = 1, c = 4))
print(matrixReshape(mat = [[1,2],[3,4]], r = 2, c = 4))
