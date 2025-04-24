from collections import defaultdict
from fprintx import printx




def totalFruit(fruits):
    counts = defaultdict(int)
    l = r = max_length = 0
    n = len(fruits)
    while r < n:
        counts[fruits[r]] += 1
        while len(counts) > 2:
            counts[fruits[l]] -= 1
            if counts[fruits[l]] == 0:
                del counts[fruits[l]]
            l += 1
        max_length = max(max_length, r - l + 1)
        r += 1

    return max_length
 



print(totalFruit(fruits = [1,2,1]))
print(totalFruit(fruits = [0,1,2,2]))
print(totalFruit(fruits = [1,2,3,2,2]))
