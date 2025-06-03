from typing import List
from fprintx import printx



def check(nums: List[int], k: int) -> int:
    l = r = s_length = s_sum = max_sum = 0
    n  = len(nums)
    while r < n:
        while l < n and s_length > k:
            s_sum -= nums[l]
            l += 1
            s_length = r-l+1
        s_sum += nums[r]
        max_sum = max(max_sum, s_sum)
        r += 1
        s_length = r-l+1

        # printx(l, r, s_length, s_sum, max_sum)

    return max_sum


print(check([1, 2, 3, 4, 5], 2))  # Expected: 9
print(check([5, -1, 5, -1, 5], 3))  # Expected: 9
print(check([], 3))  # Expected: 0
