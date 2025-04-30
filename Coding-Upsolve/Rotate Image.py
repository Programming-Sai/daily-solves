from fprintx import printx

def rotate(matrix):
        row_length, col_length = len(matrix), len(matrix[0]), 
        already_swapped = set()
        # output = [[matrix[c][r] for c in range(row_length)] for r in range(col_length)]
        
        for r in range(col_length):
            for c in range(row_length):
                if (c, r) in already_swapped:
                     continue
                
                # printx(r, c, "<-->", c, r, " | ", matrix[r][c], "<-->", matrix[c][r], already_swapped, widths=[5])
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
                already_swapped.add((r, c))

        for row in range(row_length):
             matrix[row] = matrix[row][::-1]

matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(matrix, "Before")
rotate(matrix)
print(matrix, "AFter")