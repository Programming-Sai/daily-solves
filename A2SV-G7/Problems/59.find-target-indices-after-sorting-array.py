def targetIndices(nums, target):
    res = []
    for idx, num in enumerate(sorted(nums)):
        if num == target:
            res.append(idx)
    return res