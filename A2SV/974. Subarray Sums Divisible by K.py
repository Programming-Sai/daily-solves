from collections import defaultdict
from fprintx import printx


def subarraysDivByK(nums, k):
    subarr_count = running_sum = 0
    number_of_occureneces = defaultdict(int)
    number_of_occureneces[0] += 1
    for num in nums:
        running_sum += num
        subarr_count += number_of_occureneces[running_sum % k]
        number_of_occureneces[running_sum % k] += 1
        # printx(running_sum, subarr_count, number_of_occureneces, num)
    
    return subarr_count


print(subarraysDivByK(nums = [4,5,0,-2,-3,1], k = 5))
# print(subarraysDivByK(nums = [5], k = 9))