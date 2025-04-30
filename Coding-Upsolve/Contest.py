def deleteGreatestValue(grid):
        answer = 0

        for i in range(len(grid)):
            grid[i].sort(reverse=True)

        for j in range(len(grid[0])):
            max_cell = 0
            for i in range(len(grid)):
                max_cell = max(max_cell, grid[i][j])
            answer += max_cell
        
        return (answer)



grid = [[1,2,4],[3,3,1]]

print(deleteGreatestValue(grid))
