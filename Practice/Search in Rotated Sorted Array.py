from fprintx import printx
from typing import List

def bin_search(arr, target):
    # print(arr, target)
    l , r = 0, len(arr)-1
    while l <= r:
        mid = l + (r-l)//2
        # printx(l, mid, r, arr, arr[mid], widths=[6])
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            r = mid-1
        else: 
            l = mid+1
    return -1


def check(nums: List[int], target: int) -> int:
    """
    Searches for target in a rotated sorted array nums and
    returns its index, or -1 if not found.
    """
    pivot = 0
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            pivot = i
            break
        
    left_search = bin_search(nums[:pivot+1], target)
    right_search = bin_search(nums[pivot+1:], target)
    # print(left_search, right_search)

    if left_search != -1:
        return left_search
    elif right_search != -1:
        return right_search+pivot+1
    else:
        return -1



print(check([4,5,6,7,0,1,2], 0))   # Expected: 4
# Explanation: 0 is at index 4.

print(check([4,5,6,7,0,1,2], 3))   # Expected: -1
# Explanation: 3 isn’t in nums.

print(check([1], 0))             # Expected: -1
# Single‑element array without the target.

print(check([], 5))              # Expected: -1
# Empty array.

print(check([1,2], 1))           # Expected: 0
# Small array where no rotation occurs.

print(check([2,1], 1))           # Expected: 1
# Two‑element rotated array.
