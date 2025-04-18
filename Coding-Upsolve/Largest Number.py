
from functools import cmp_to_key


def largestNumber(nums):
        return int("".join([str(i) for i in sorted(nums, key=cmp_to_key(lambda a, b : -1 if str(a) + str(b) > str(b) + str(a) else 1 if str(a) + str(b) < str(b) + str(a) else 0 if str(a) + str(b) == str(b) + str(a) else ''))]))




# nums = [3, 30, 34, 5, 9]
# print()

    



print(largestNumber(nums = [10,2]))
print(largestNumber(nums = [3,30,34,5,9]))
print(largestNumber(nums = [432,43243]))
print(largestNumber(nums = [0,0]))