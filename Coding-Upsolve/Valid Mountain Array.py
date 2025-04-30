def validMountainArray(arr):
    peak = max(arr)
    peak_index = 0
    for idx, i in enumerate(arr):
        if i == peak:
            peak_index = idx
            break
    # Checking if we are starting from the peak
    if arr[0] == peak or arr[-1] == peak:
        return False
    
    # Checking ascending steepness
    ascent = arr[ : peak_index]
    for idx, i in enumerate(ascent):
        if idx == 0:
            continue
        else:
            if i > ascent[idx - 1]:
                continue
            else:
                return False
            
    # Checking descending steepness
    descent=arr[peak_index + 1:]
    for idx, i in enumerate(descent):
        if idx == len(descent) - 1:
            break
        else:
            if i > descent[idx + 1]:
                continue
            else:
                return False
            
    return True
            


n=int(input())
arr = list(map(int, input().split()))
print(validMountainArray(arr))
# print(validMountainArray(arr = [3,5,5]))