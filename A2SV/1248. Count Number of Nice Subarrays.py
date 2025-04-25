from collections import defaultdict
from itertools import accumulate
from fprintx import printx


def numberOfSubarrays(nums, k):
    # l = r = odd_count = subarr_count = 0
    # n = len(nums)
    # while r < n:
    #     if nums[r] % 2 != 0:
    #         odd_count += 1
    #     met_odd = False
    #     while odd_count == k:
    #         # if odd_count == k:
    #         met_odd = met_odd or (odd_count == k)
    #         odd_count -= 1
    #         l += 1
    #     subarr_count += met_odd
    #     printx(nums[l:r+1], odd_count, l, r, met_odd, subarr_count, widths=[27])
    #     r += 1
    # return odd_count
    nums[:] = [0 if i%2==0 else 1 for i in nums]
    prefix_nums = list(accumulate(nums))
    prefix_seen_before = defaultdict(int)
    prefix_seen_before[0] += 1
    print(nums, prefix_nums, dict(prefix_seen_before))
            


# print(numberOfSubarrays(nums = [1,1,2,1,1], k = 3))
# print(numberOfSubarrays(nums = [2,4,6], k = 1))
print(numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2))