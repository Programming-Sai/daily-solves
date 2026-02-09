class Solution:
    def isCovered(self, ranges, left, right):
        range_array = set()
        for x, y in ranges:
            range_array.update(range(x, y+1))
        return set(range(left, right+1)).issubset(range_array)