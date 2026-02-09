#User function Template for python3
from collections import Counter
def isSubset(a, b):
        counter_a = Counter(a)
        counter_b = Counter(b)
        for k, v in counter_b.items():
            if k not in counter_a or counter_a[k] < v:
                print(k, counter_a, counter_a[k], v)
                return False
        return True
    
    
    
    
print(isSubset([11, 7, 1, 13, 21, 3, 7, 3], [11, 3 , 1, 7]))