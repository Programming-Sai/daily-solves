
def diag(matrix):
    m=len(matrix)
    n=len(matrix[0])
    for d in range(m + n - 1):
        if d % 2 != 0:
            for i in range(max(0, d - n + 1), min(m, d + 1)):
                j = d - i
                print(matrix[i][j])
        else:
            for i in range(min(m, d + 1), (max(0, d - n + 1) - 1), -1):
                j = d - i
                print(matrix[i][j])


def findDiagonalOrder(mat):
    if not mat: return []

    m, n = len(mat), len(mat[0])
    result = []
    
    for d in range(m + n - 1):
        intermediate = []

        # Determine starting point of diagonal
        r = 0 if d < n else d - n + 1
        c = d if d < n else n - 1

        while r < m and c >= 0:
            intermediate.append(mat[r][c])
            r += 1
            c -= 1

        if d % 2 == 0:
            result.extend(intermediate[::-1])
        else:
            result.extend(intermediate)
    
    return result



print(findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))