from collections import defaultdict
from typing import List
from fprintx import printx

def check(nums: List[int]) -> int:
    """
    Given a list of integers `nums`, return the majority element.
    The majority element is the one that appears more than n // 2 times.
    You may assume that the majority element always exists.
    """
    counter = defaultdict(int)
    n = len(nums)
    for num in nums:
        counter[num] += 1
        printx(counter, counter[num], num, widths=[n])
        if counter[num] > n//2:
            return num
        



print(check([3, 2, 3]))  
# Expected: 3

print(check([2, 2, 1, 1, 1, 2, 2]))  
# Expected: 2

print(check([1, 1, 1, 2, 3]))  
# Expected: 1

print(check([1]))  
# Expected: 1 — Only one element

print(check([7, 7, 7, 7]))  
# Expected: 7 — All same elements

print(check([9, 1, 9, 1, 9]))  
# Expected: 9 — Majority at odd positions
