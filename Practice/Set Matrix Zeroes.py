from typing import List
from fprintx import printx

def set_zero(matrix, r, c):
    # Setting Row
    for i in range(len(matrix[r])):
        matrix[r][i] = 0

    # Setting Columns
    for i in range(len(matrix)):
        # printx(matrix[i][c], matrix[c][r], r, c)
        matrix[i][c] = 0

def check(matrix: List[List[int]]) -> None:
    """
    Given a `m x n` matrix, if an element is 0, set its entire row and column to 0.
    Do it in-place.

    Modifies the matrix directly. No return.
    """
    m, n, zeros = len(matrix), len(matrix[0]), []
    for r in range(m):
        for c in range(n):
            if matrix[r][c] == 0:
                zeros.append((r, c))

    for cell in zeros:
        set_zero(matrix, *cell)
    



m = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
check(m)
print(m)
# Expected: [[1,0,1], [0,0,0], [1,0,1]]

m = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
check(m)
print(m)
# Expected: [[0,0,0,0], [0,4,5,0], [0,3,1,0]]

m = [[1]]
check(m)
print(m)
# Expected: [[1]]

m = [[0]]
check(m)
print(m)
# Expected: [[0]]

m = [[1,0]]
check(m)
print(m)
# Expected: [[0,0]]
