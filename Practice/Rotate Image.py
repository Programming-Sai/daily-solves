from fprintx import printx


from typing import List

def check(matrix: List[List[int]]) -> None:
    """
    You are given an n x n 2D matrix representing an image, rotate the image 
    by 90 degrees (clockwise) in-place.

    Do not return anything, modify the matrix in-place.
    """
    n = len(matrix)
    m = len(matrix[0])
    visited = set()
    for r in range(n):
        for c in range(m):
            if r == c or (r, c) in visited or (c, r) in visited: continue
            # printx(r, c, matrix[r][c], matrix[c][r])
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            # print()
            visited.add((r, c))
            visited.add((c, r))
            # printx(r, c, matrix[r][c], matrix[c][r])


    # printx(*matrix)
    for row in range(n):
        matrix[row][:] = matrix[row][::-1]





m = [[1,2,3],[4,5,6],[7,8,9]]
check(m)
print(m)  # Expected: [[7,4,1],[8,5,2],[9,6,3]]

m = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
check(m)
print(m)
# Expected: [
#   [15,13,2,5],
#   [14,3,4,1],
#   [12,6,8,9],
#   [16,7,10,11]
# ]

m = [[1]]
check(m)
print(m)  # Expected: [[1]]

m = [[1, 2], [3, 4]]
check(m)
print(m)  # Expected: [[3,1],[4,2]]
