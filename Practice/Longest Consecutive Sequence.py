from fprintx import printx


from typing import List

def check(nums: List[int]) -> int:
    """
    Given an unsorted array of integers `nums`, return the length of the longest 
    consecutive elements sequence.

    You must write an algorithm that runs in O(n) time.
    """
    if not nums: return 0
    nums_set = set(nums)
    res = 0
    for num in nums_set:
        if num - 1 not in nums_set:
            res = 1
            continue
        if (num + 1 in nums_set or num - 1 in nums_set):
            res += 1
    return res or 1





print(check([100, 4, 200, 1, 3, 2]))  
# Expected: 4 (sequence: 1, 2, 3, 4)

print(check([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  
# Expected: 9 (sequence: 0 through 8)

print(check([10, 30, 20]))  
# Expected: 1 (no consecutive sequence)

print(check([]))  
# Expected: 0 — No elements

print(check([5]))  
# Expected: 1 — Single element

print(check([1, 2, 0, 1]))  
# Expected: 3 (sequence: 0, 1, 2 — duplicate ignored)


