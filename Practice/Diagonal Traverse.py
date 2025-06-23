from typing import List

def check(matrix: List[List[int]]) -> List[int]:
    """
    Given an m x n matrix, return all elements of the matrix in a diagonal order.

    The traversal should zig-zag from top-left to bottom-right like this:
    Input:
    [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]
    
    Output:
    [1,2,4,7,5,3,6,8,9]
    """
    result = []
    n, m = len(matrix), len(matrix[0])

    for diag in range(n+m-1):
        inter = []
        for r in range(n):
            # print(r, diag - r) if 0 <= (diag - r) < m else ""
            inter.append(matrix[r][diag-r]) if 0 <= (diag - r) < m else ""
        if diag % 2:
            result.extend(inter)
        else:
            result.extend(inter[::-1])
    return result




print(check([[1,2,3],[4,5,6],[7,8,9]]))  # [1,2,4,7,5,3,6,8,9]
print(check([[1,2],[3,4]]))              # [1,2,3,4]
print(check([[1]]))                      # [1]
print(check([[1,2,3],[4,5,6],[7,8,9]]))  # [1,2,4,7,5,3,6,8,9]
print(check([[1,2],[3,4]]))              # [1,2,3,4]
print(check([[1]]))                      # [1]
print(check([[1, 2, 3, 4, 5],[6, 7, 8, 9,10],[11,12,13,14,15]])), # [1, 2, 6, 11, 7, 3, 4, 8, 12, 13, 9, 5, 10, 14, 15]
