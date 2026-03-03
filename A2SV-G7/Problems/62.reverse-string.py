
from typing import List

def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    l, r = 0, len(s)-1
    while l < r:
        s[r], s[l] = s[l], s[r]
        l+=1
        r-=1