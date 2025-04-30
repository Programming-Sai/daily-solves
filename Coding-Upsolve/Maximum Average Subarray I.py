from fprintx import printx


def findMaxAverage(nums, k):
    total_sum = sum(nums[:k])
    average = total_sum/k
    n = len(nums)
    l = 1
    r = l + k -1

    while r < n:
        total_sum = total_sum - nums[l-1] + nums[r]
        average = max(average, total_sum/k)
        # printx(total_sum, average , l, r)

        l += 1
        r += 1

        
    return average



print(findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))
print(findMaxAverage(nums = [5], k = 1))
# print(findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))
