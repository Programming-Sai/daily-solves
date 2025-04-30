def diagonalSum(mat):
    n=len(mat)
    sec_diag = [( i, n - ( i + 1) ) for i in range(n)]
    prim_diag = [(i, i) for i in range(n)]
    for i in range(n):
        if sec_diag[i] == prim_diag[i]:
            sec_diag.pop(i)
            break
    prim_diag.extend(sec_diag)
    diag = [mat[i[0]][i[1]] for i in prim_diag]
    return sum(diag)




mat1 = [[1,2,3],
        [4,5,6],
        [7,8,9]]


mat2 = [[1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]]

mat3 = [[5]]

print(diagonalSum(mat3))


