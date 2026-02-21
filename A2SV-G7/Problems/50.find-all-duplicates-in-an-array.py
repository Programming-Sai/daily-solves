def findDuplicates(nums):
    res = []
    for i in range(len(nums)):
        while nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
            correct_index = nums[i] - 1
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
    for i in range(len(nums)):
        if nums[i] != i + 1:
            res.append(nums[i])
    return res