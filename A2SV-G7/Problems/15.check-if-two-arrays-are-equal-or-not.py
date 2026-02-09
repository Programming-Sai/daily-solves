class Solution:
    def checkEqual(self, a, b) -> bool:
        if len(a) != len(b):
            return False
        return sorted(a) == sorted(b)