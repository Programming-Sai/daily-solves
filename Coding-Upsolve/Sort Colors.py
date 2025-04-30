from fprintx import printx



def sortColors(nums):
    # Implementing Counting Sort
    sorter = [0] * 3
    result = []

    for num in nums:
        sorter[num] += 1
    # print(sorter)
    
    for i, sorting in enumerate(sorter):
        result.extend([i] * sorting)
    # print(result)

    for i in range(len(nums)):
        nums[i] = result[i]

nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)