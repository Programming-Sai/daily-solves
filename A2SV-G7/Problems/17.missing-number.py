
def sol1(nums):
    nums.sort()
    for i, num in enumerate(nums):
        if i != num:
            return i
    return len(nums)
    

def sol2(nums):
    sum_nums = sum(nums)
    sum_n = sum([i for i in range(len(nums)+1)])
    return sum_n - sum_nums
   
print(sol1([3,0,1]))
print(sol2([0,1]))