from fprintx import printx

# def countPairs(nums, k):
#     count = 0
#     i, j = 0, len(nums)-1
#     while i < j:
#         if (nums[i] == nums[j]) and ((i*j) % k == 0):
#             count += 1
    
#         i += 1
#         j -= 1

#     return count


def countPairs(nums, k):
    if len(set(nums)) == len(nums):
        return 0
    
    count = 0
    already_ckecked = set()
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i >= j:
                continue
            if (nums[i] == nums[j]) and ((i*j) % k == 0):
                count += 1
                already_ckecked.add((i, j))
                # printx(i, j, nums[i], nums[j], count, already_ckecked, widths=[5])

    return count




print(countPairs(nums = [3,1,2,2,2,1,3], k = 2))
print(countPairs(nums = [1,2,3,4], k = 1))