from collections import defaultdict
from fprintx import printx


def subarraySum(nums, k):
    # l = r = subarr_count = k_count = 0
    # n = len(nums)
    # while r < n:
    #     k_count += nums[r]
    #     met_k = False

    #     while ((k_count >= k) or (k_count <= k and k == 0)) and l < n:
    #         met_k = met_k or (k_count == k)
    #         k_count -= nums[l]
    #         l += 1
    #     subarr_count += met_k
    #     r += 1
    #     printx(l, r, nums[l:r+1], subarr_count, k_count, met_k, widths=[8])
    # return subarr_count
    subarr_count = running_sum = 0
    prefix_sum_occurences_count = defaultdict(int)
    prefix_sum_occurences_count[0] = 1
    for num in nums:
        running_sum += num
        subarr_count += prefix_sum_occurences_count[running_sum - k]
        prefix_sum_occurences_count[running_sum] += 1
    return subarr_count
    


print(subarraySum(nums = [1,1,1], k = 2))
print(subarraySum(nums = [1,2,3], k = 3))
print(subarraySum(nums = [1], k = 0))
print(subarraySum(nums = [], k = 3))
print(subarraySum(nums = [-1, -1, 1], k = 0))
print(subarraySum(nums = [-1, -1, 1], k = 1))