from typing import List

def check(nums: List[int]) -> int:
    """
    Given an array of integers `nums`, return the pivot index such that the 
    sum of all the numbers to the left of the index is equal to the sum of 
    all the numbers to the right of the index.
    
    If no such index exists, return -1. If there are multiple, return the left-most.
    """
    prefix_sum = [0] * (len(nums)+1)
    for i in range (len(nums)):
        prefix_sum[i+1] = prefix_sum[i] + nums[i]

    for i in range(len(nums)):
        if prefix_sum[i] == (prefix_sum[-1] - prefix_sum[i+1]):
            return i
    return -1







print(check([1, 7, 3, 6, 5, 6]))  
# Expected: 3  
# Left sum = 11, right sum = 11

print(check([2, 1, -1]))  
# Expected: 0  
# Left sum = 0, right sum = 0

print(check([1, 2, 3]))  
# Expected: -1  
# No valid pivot index


print(check([0]))  
# Expected: 0  
# Only one element, both sides are "empty" = 0

print(check([]))  
# Expected: -1  
# No index at all

print(check([-1, -1, -1, 0, 1, 1]))  
# Expected: 0  
# Left = 0, Right = rest = -1 + -1 + 0 + 1 + 1 = 0
