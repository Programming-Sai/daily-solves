'''
WTF is wrong with this solution??
'''


# def check(matrix):
#     row = 0
#     for i in range(1, len(matrix)-1):
#         if matrix[i].count('#') == 1 :
#             row = i
#             break
#     for i in range(len(matrix[row])):
#         if matrix[row][i] == '#':
#             return row+1, i+1



        
def check(matrix):
    counts = []
    # counts = [-1]
    for i in range(len(matrix)):
        counts.append(matrix[i].count('#'))
    # counts.append(-1)

    # print(*counts)
    row = 0
    for i in range(1, len(counts)-1):
        if counts[i] == 1 and counts[i-1] == 2 and counts[i+1] == 2:
            row = i
            break
    
    for i in range(1, len(matrix[row])-1):
        if matrix[row][i] == '#':
            return row+1, i+1
    



# Read entire input at once
import sys
lines = [line.strip() for line in sys.stdin if line.strip()]

t = int(lines[0])
ptr = 1

for _ in range(t):
    matrix = lines[ptr:ptr+8]
    ptr += 8
    print(*check(matrix))