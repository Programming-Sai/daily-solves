def containsDuplicate(nums):
    return not(len(set(nums)) == len(nums))