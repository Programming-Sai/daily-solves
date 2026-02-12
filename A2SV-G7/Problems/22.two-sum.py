

def twoSum(nums, target):
    c_t = {}
    for i, num in enumerate(nums):
        print(c_t)
        complement = target - num
        if complement in c_t:
            return i, c_t[complement]
        c_t[num] = i


print(twoSum([2,7,11,15], 9))