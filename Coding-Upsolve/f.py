def deleteGreatestValue(grid):
    answer = 0
    for r in range(len(grid)):
        max_row = max(r)
        for c in range(len(r)):
           if grid[r][c] == max_row:
               grid[r][c] = float("-inf")
                

