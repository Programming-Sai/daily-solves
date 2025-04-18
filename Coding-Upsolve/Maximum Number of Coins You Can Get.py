from fprintx import printx


def maxCoins(piles):
        piles = sorted(piles, reverse=True)
        exclusions = (len(piles) // 3) 
        max_sum = 0
        for i in range(len(piles[:(len(piles) - exclusions)])):
            if i % 2 == 0:
                continue
            max_sum += piles[i]
        return max_sum


print(maxCoins(piles = [2,4,1,2,7,8]))
# print(maxCoins(piles = [2,4,5]))
# print(maxCoins(piles = [9,8,7,6,5,1,2,3,4]))
