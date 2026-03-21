class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        arr = sorted(set(nums))
        res = 0
        for i in range(len(arr)):
            res += (i * freq[arr[i]])
        return res