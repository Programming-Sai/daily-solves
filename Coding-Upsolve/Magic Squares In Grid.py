from fprintx import printx


def numMagicSquaresInside(grid):
    row_len = len(grid)
    col_len = len(grid[0])

    if row_len < 3 or col_len < 3:
        return 0
    count = 0
    for r in range(row_len -2):
        for c in range(col_len - 2):
            count += check_grid_validity(r, c, grid)
            print(count)
    return(count)
        

def check_grid_validity(r, c, grid):
    #   Check uniqueness
    unique_set = set()
    for i in range(3):
          for j in range(3):
            if 1 > grid[r+i][c+j] or grid[r+i][c+j] > 9 or grid[r+i][c+j] in unique_set:
                 return False
            unique_set.add(grid[r+i][c+j])

    # Check row sum
    row_sums = set()
    for i in range(3):
        row_sums.add(sum(grid[r+i][c:c+3]))
    if len(row_sums) != 1:
         return False
    
    # Check col sum
    col_sums = set()
    for j in range(3):
        col_sums.add(sum(grid[r+i][c+j] for i in range(3)))

    if len(col_sums) != 1:
         return False
    
    target = row_sums.pop()
    if col_sums.pop() != target:
        return False
    
    # Check Diagonals
    m_diag_count = sum(grid[r+i][c+i] for i in range(3))
    mi_diag_count = sum(grid[r+i][c+2-i] for i in range(3))

    if m_diag_count != target or mi_diag_count != target:
        return False

    return True



# print(numMagicSquaresInside(grid = [
#                                      [4,3,8,4],
#                                      [9,5,1,9],
#                                     #  [9,5,1,9],
#                                      [2,7,6,2]
#                                 ]))

# print(numMagicSquaresInside(grid = [[8]]))
print(numMagicSquaresInside(grid = [
                                        [3,2,9,2,7],
                                        [6,1,8,4,2],
                                        [7,5,3,2,7],
                                        [2,9,4,9,6],
                                        [4,3,8,2,5]
                            ]))