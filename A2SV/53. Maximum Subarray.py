from fprintx import printx


def maxSubArray(nums):
    # if len(nums) == 1:
        # return nums[0]
    running_sum = 0
    max_sum_so_far = nums[0]

    for num in nums:
        running_sum += num
        if max_sum_so_far < running_sum:
            max_sum_so_far = running_sum
        # max_sum_so_far = max(max_sum_so_far, (running_sum))
        if running_sum < 0:
            running_sum = 0
        # printx(running_sum, min_sum_so_far, max_sum_so_far, num)

    return  max_sum_so_far


print(maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray(nums = [-1]))
print(maxSubArray(nums = [1]))
print(maxSubArray(nums = [5,4,-1,7,8]))
print(maxSubArray(nums = [-2,-1]))