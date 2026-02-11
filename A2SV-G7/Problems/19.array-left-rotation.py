def rotateLeft(d, arr):
    left_chunk = arr[:d]
    right_chunk = arr[d:]
    return(right_chunk+left_chunk)




print(rotateLeft(4, [1, 2, 3, 4, 5]))
print(rotateLeft(2, [1, 2, 3, 4, 5]))