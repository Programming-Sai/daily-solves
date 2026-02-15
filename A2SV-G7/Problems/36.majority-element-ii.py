from collections import Counter

def majorityElement(nums):
    counts = Counter(nums)
    result = []
    n = len(nums)
    for k, v in counts.items():
        if v > (n//3):
            result.append(k)
    return result