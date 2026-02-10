
def sol(nums):
    nums.sort()
    for i, num in enumerate(nums):
        if i != num:
            return i
    return len(nums)
    


print(sol([3,0,1]))
print(sol([0,1]))