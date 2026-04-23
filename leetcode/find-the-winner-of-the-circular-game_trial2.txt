class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def win(n):
            if n == 1:
                return 0
            return (win(n - 1) + k) % n
        return win(n)+1
        
        
