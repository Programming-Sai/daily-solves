from collections import defaultdict

def countPairs(nums, k):
    count = 0
    seen_map = defaultdict(list)
    for i, num in enumerate(nums):
        for j in seen_map[num]:
            if ((i * j) % k) == 0:
                count += 1
        seen_map[num].append(i)
    return count