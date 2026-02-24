def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    m, n, seen = len(matrix), len(matrix[0]), set()
    for r in range(m):
        for c in range(n):
            if (r, c) not in seen and (c, r) not in seen:
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
                seen.add((r, c))

    for row in matrix:
        row.reverse()

    