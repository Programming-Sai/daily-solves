class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x < 10: return True

        original = x
        reversed = 0
        while x > 0:
            digit = x % 10
            reversed = (reversed * 10) + digit
            x = x // 10

        print(original, reversed)
        return original == reversed