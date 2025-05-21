from fprintx import printx

def gridGame(grid):
    n = len(grid[0])
    top_row_prefix_sum = [0] * (n+1)
    bottom_row_prefix_sum = [0] * (n+1)

    for i in range(1, n+1):
        top_row_prefix_sum[i] = top_row_prefix_sum[i - 1] + grid[0][i-1]
        bottom_row_prefix_sum[i] = bottom_row_prefix_sum[i - 1] + grid[1][i-1]
    
    # printx(top_row_prefix_sum, bottom_row_prefix_sum)
    R2_score = float('inf')

    for i in range(n):
        # printx(R2_score, (top_row_prefix_sum[n] - top_row_prefix_sum[i+1]), bottom_row_prefix_sum[i], widths=[5])
        R2_score = min(R2_score, max((top_row_prefix_sum[n] - top_row_prefix_sum[i+1]), bottom_row_prefix_sum[i]))

    return R2_score


print(gridGame( grid = [[2,5,4],[1,5,1]]))
print(gridGame( grid = [[3,3,1],[8,5,2]]))
print(gridGame( grid = [[1,3,1,15],[1,3,3,1]]))
print(gridGame( grid = [[1,3,1,15],[1,3,3,1]]))
print(gridGame( grid = [[1,3,1,15],[1,3,3,1]]))