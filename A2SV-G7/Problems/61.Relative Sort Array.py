from collections import Counter
from typing import List

def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
    counts = Counter(arr1)
    set_arr_2 = set(arr2)
    remaining = []
    res = []
    for ar in arr2:
        res.extend([ar] * counts[ar])
    for ar in arr1:
        if ar not in set_arr_2:
            remaining.append(ar)
    return res + sorted(remaining)