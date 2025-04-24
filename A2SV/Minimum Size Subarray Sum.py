from fprintx import printx



def minSubArrayLen(target, nums):
    n = len(nums)
    l = r  = current_sum = 0
    min_length = float('inf')
    while r < n:
        current_sum += nums[r]
        while current_sum >= target:
            current_sum -= nums[l]
            min_length = min(min_length, (r-l+1))
            l += 1
        r += 1
    return 0 if min_length == float('inf') else min_length


print(minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))
print(minSubArrayLen(target = 4, nums = [1,4,4]))
print(minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]))