def isToeplitzMatrix(matrix):
    for r in range(1, len(matrix)):
        for c in range(1, len(matrix[r])):
            if matrix[r][c] != matrix[r-1][c-1]:
                return False
        
    return True

print(isToeplitzMatrix(matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
print(isToeplitzMatrix(matrix = [[1,2],[2,2]]))

