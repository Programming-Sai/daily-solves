from collections import Counter

def counter(arr):
    count = Counter()
    
    for num in arr:
        count[num] += 1
        if count[num] == 3:  
            return num

    return -1  

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(counter(arr))
