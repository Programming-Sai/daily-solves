from fprintx import printx

def ziggity(matrix):
    row_len = len(matrix)
    result = []

    for r in range(row_len):
        result += (matrix[r] if r % 2 == 0 else matrix[r][::-1])

    return result


def transpose(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])
    already_swapped = set()

    for r in range(row_len):
        for c in range(col_len):
            if (r, c) in already_swapped:
                continue
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            already_swapped.add((c, r))
            # printx(r, c, already_swapped, widths=[10])

    return matrix


def diag(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])
    result = []
    for diags in range((row_len + col_len) - 1):
        for r in range(row_len):
            if 0 <= r < row_len and 0 <= (diags - r) < col_len:
                printx(diags, r, result, widths=[10])
                result.append(matrix[r][diags - r])

    return result



def diag_reverse(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])
    result = []
    for diags in range(-(col_len - 1), row_len):
        for r in range(row_len):
            if 0 <= r < row_len and 0 <= (r - diags) < col_len:
                printx(diags, r, result, widths=[10])
                result.append(matrix[r][r - diags])

    return result





def spiral(matrix):
    top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
    result = []
    while top <= bottom and left <= right:
        for c in range(left, right+1):
            # printx(top, c)
            result.append(matrix[top][c])
        top += 1

        for r in range(top, bottom+1):
            # printx(r, right)
            result.append(matrix[r][right])
        right -= 1

        if top <= bottom:
            for c in range(right, left-1, -1):
                # printx(old_bottom, c)
                result.append(matrix[bottom][c])
            bottom -= 1
        if left <= right:
            for r in range(bottom, top-1, -1):
                # printx(r, left)
                result.append(matrix[r][left])
            left += 1

    return result


def diag_traversal(matrix):
        row_len = len(matrix)
        col_len = len(matrix[0])
        result = []
        for diags in range((row_len + col_len) - 1):
            for r in range(row_len):
                if diags % 2 != 0:
                    if 0 <= r < row_len and 0 <= (diags - r) < col_len:
                        result.append(matrix[r][diags - r])
                else:
                    if 0 <= r < col_len  and 0 <= (diags - r) < row_len:
                        result.append(matrix[diags - r][r])
        return result



def eigtht_traversal(matrix):
    top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
    result = []
    while top <= bottom and left <= right:
        
        for c in range(left, right+1):
            result.append(matrix[top][c])
            printx(top, c)
        top += 1
        print("===  ->")


        for r in range(top):
            # if top == c:
                result.append(matrix[top][right - r-1])
                printx(top, right - r-1)
        top += 1
        print("===  /")
        


        for c in range(left, right+1):
            result.append(matrix[bottom][c])
            printx(bottom, c)
        bottom -= 1
        print("===  ->")

        for c in range(left, right+1):
            if bottom == c:
                result.append(matrix[top][c])
                printx(bottom, c)
        top += 1
        print("===  \\")





matrix=[
    [1,   2,    3,  4],
    [5,   6,    7,  8],
    [9,   10,  11,  12],
    [13,  14,  15,  16],
]
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# matrix = [[6,9,7]]
# mat = [[6,9,7]]
# matrix = [[2,3]]
# print(ziggity(matrix))
# print(transpose(matrix))
# print(diag(matrix))
# print(diag_reverse(matrix))
# print(diag_traversal(matrix))
# print(spiral(matrix))
print(eigtht_traversal(matrix))