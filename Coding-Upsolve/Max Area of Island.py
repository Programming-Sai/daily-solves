def maxAreaOfIsland(grid):
    searched_set = set()
    max_island=0

    for i in range(len(grid)):
        island_area_counter = 0
        for j in range(len(grid[0])):
            if grid[i][j] == 0 or (i, j) in searched_set:
                continue
            scan_neighbour(grid, i, j, island_area_counter, searched_set)




def scan_neighbour(grid, i, j, counter, searched_set):
    offsets = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    if all(grid[x][y] in searched_set or grid[x][y] == 0 for x, y in offsets):
        return counter
    
    for offset_i, offset_j in offsets:
        if not valid_bounds(offset_i, j + offset_j, len(grid), len(grid[0])):
            continue


        if grid[i + offset_i][j + offset_j] == 0:
            searched_set.update((i + offset_i, j + offset_j))
            continue
        elif grid[i + offset_i][j + offset_j] not in searched_set and grid[j + offset_j][j + offset_j] == 1:
            scan_neighbour(grid, i + offset_i, j + offset_j, counter + 1, searched_set)
        else:
            return counter



def valid_bounds(i, j, m, n):
    if 0 <= i < m and 0 <= j < n:
        return True
    return False

        





print(maxAreaOfIsland(grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]))