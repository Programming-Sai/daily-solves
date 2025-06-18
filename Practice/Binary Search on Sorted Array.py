from typing import List

def check(nums: List[int], target: int) -> int:
    """
    You are given a sorted array `nums` (ascending). Return the index of `target` using binary search.
    If the target is not found, return -1.
    """
    left, right= 0, len(nums)-1
    while left <= right:
        mid = left + (right -left)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid -1
        else:
            left = mid + 1
    return -1




print(check([1, 2, 3, 4, 5], 3))  
# Expected: 2

print(check([1, 2, 3, 4, 5], 1))  
# Expected: 0

print(check([1, 2, 3, 4, 5], 5))  
# Expected: 4


print(check([], 4))  
# Expected: -1  
# No elements at all

print(check([1], 1))  
# Expected: 0  
# Single element, it's the target

print(check([1, 2, 3], 0))  
# Expected: -1  
# Target is smaller than all elements
