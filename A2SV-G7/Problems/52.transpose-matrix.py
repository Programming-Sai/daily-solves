def transpose(matrix):
    m, n = len(matrix), len(matrix[0])
    res = [[None for _ in range(m)] for _ in range(n)]
    for r in range(m):
        for c in range(n):
            res[c][r] = matrix[r][c]

    return res