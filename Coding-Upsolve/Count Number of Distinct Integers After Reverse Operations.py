def countDistinctIntegers(nums):
        res_set = set(nums)

        for num in nums:
            if num > 10:
                res_set.add(int(str(num)[::-1]))
        
        return len(res_set)


print(countDistinctIntegers(nums = [1,13,10,12,31]))
print(countDistinctIntegers(nums = [2,2,2]))

