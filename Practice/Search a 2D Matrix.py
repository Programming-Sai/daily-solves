from fprintx import printx


def check(matrix, target):
    if not matrix or not matrix[0]:
        return False
    m = len(matrix)
    n = len(matrix[0])
    l = 0
    r = m*n-1

    while l <= r:
        mid = l + (r-l)//2
        row = mid // n
        col = mid % n
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            r = mid - 1
        else:
            l = mid + 1
    return False



print(check(matrix=[
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
], target=3))  # Expected: True


print(check(matrix=[
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
], target=13))  # Expected: False


print(check(matrix=[
  [1]
], target=1))  # Expected: True


print(check([], target=1))  # should be False
print(check([[]], target=1))  # should also be False
