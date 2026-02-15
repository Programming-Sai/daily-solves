from collections import defaultdict

def smallerNumbersThanCurrent(nums):
    sorted_nums = sorted(nums, reverse=True)
    num_less = defaultdict(int)
    n = len(nums)
    res = [None for _ in range(n)]
    for i, num in enumerate(sorted_nums):
        num_less[num] = n - i - 1
    for i in range(n):
        res[i] = num_less[nums[i]]
    return res