from fprintx import printx


def targetIndices(nums, target):
    output = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] == target:
            output.append(i)
        
    return output


print(targetIndices(nums = [1,2,5,2,3], target = 2))
print(targetIndices(nums = [1,2,5,2,3], target = 3))
print(targetIndices( nums = [1,2,5,2,3], target = 5))



    