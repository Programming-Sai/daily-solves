from fprintx import printx
from typing import List

def check(nums: List[int]) -> List[int]:
    stack = []
    n = len(nums)
    result = [-1] * n
    for i in range(2*n):
        while stack and nums[stack[-1]] < nums[i%n]:
            top = stack.pop()
            result[top] = nums[i%n]
        stack.append(i%n)

    return result


print(check([1, 2, 1]))  # Expected: [2, -1, 2]
print(check([1, 2, 3, 4, 3]))  # Expected: [2, 3, 4, -1, 4]
print(check([3, 8, 4, 1, 2]))  # Expected: [8, -1, 8, 2, 3]
print(check([]))  # Expected: []
print(check([2]))  # Expected: [-1]