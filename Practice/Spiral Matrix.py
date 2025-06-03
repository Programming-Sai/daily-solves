from typing import List
from fprintx import printx


def check(matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []
    top = left = 0
    bottom = len(matrix) - 1
    right = len(matrix[0]) - 1
    result = []
    while top <= bottom and left <= right:
        # if left <= right:
        for i in range(left, right+1):
                result.append(matrix[top][i])
        top += 1

        # if top <= bottom:
        for j in range(top, bottom+1):
                result.append(matrix[j][right])
        right -= 1

        if top <= bottom:
            for k in range(right, left - 1, -1):
                result.append(matrix[bottom][k])
            bottom -= 1

        if  left <= right:  
            for l in range(bottom, top - 1, -1):
                result.append(matrix[l][left])
            left += 1

    return result




print(check([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [10, 11, 12]
]))  # Expected: [1, 2, 3, 6, 9, 8, 7, 4, 5]

print(check([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12]
]))  # Expected: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


print(check([[]])) # Expected []