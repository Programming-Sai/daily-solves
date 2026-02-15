from collections import Counter

def majorityElement(nums):
    counts=Counter(nums)
    return max(counts, key=counts.get)