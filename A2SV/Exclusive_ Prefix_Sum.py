
def runningSum(nums):
    running_sum = [0] * len(nums)
    # running_sum[0] = (nums[0])
    for i in range(1, len(nums)):
        running_sum[i] = running_sum[i-1] + nums[i - 1]
    return running_sum



print(runningSum([3, 1, 7, 0, 4, 1, 6, 3]))