class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, n, max_area = 0, len(height)-1, len(height), float("-inf")
        while l < r:
            max_area = max(max_area, ((r - l) * (min(height[l], height[r]))))
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return max_area