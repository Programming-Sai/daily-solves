from typing import List
from fprintx import printx



def check(stream: List[int], k: int) -> List[float]:
    """
    Given a stream of integers and a window size k,
    return the moving average for each new element.
    """
    l = r = counter = 0
    n = len(stream)
    result = []
    while r < n:
        counter += stream[r]
        while l < n and (r-l+1) > k:
            counter -= stream[l]
            l += 1
        if (r - l + 1) == k:
            result.append(counter / k)
        r += 1
    return result



print(check([1, 10, 3, 5], 3))  
# Expected: [1.0, (1+10)/2, (1+10+3)/3, (10+3+5)/3]
#          [1.0, 5.5,     4.6667,      6.0]

print(check([4, 0, -1, 3, 10], 1))  
# Expected: [4.0, 0.0, -1.0, 3.0, 10.0]
# Window size 1 → each element alone.

print(check([], 3))               
# Expected: []
# No stream → no averages.

print(check([5,8], 5))           
# Expected: [5.0, (5+8)/2]
# Window larger than stream length.
