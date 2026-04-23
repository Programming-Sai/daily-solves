class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def diff(l, r, nums):
            if l == r:
                return nums[l]
            return max(nums[l]-diff(l+1, r, nums), nums[r]-diff(l, r-1, nums))
        return diff(0, len(nums)-1, nums) >= 0
