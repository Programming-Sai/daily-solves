from fprintx import printx


def maxTurbulenceSize(arr):
    n = len(arr)
    if n == 1 or len(set(arr)) == 1:
        return 1
    l, r = 0, 1
    max_length = 0
    while r < n:
        # printx(l, r, max_length, arr[r-2], arr[r-1], arr[r], widths=[4])  
        if arr[r] == arr[r - 1]:
            l = r  
        if r >= 2 and not ((arr[r-2] > arr[r-1] and arr[r-1] < arr[r]) or (arr[r-2] < arr[r-1] and arr[r-1] > arr[r])):
            l = r - 1
        max_length = max(max_length, r-l+1)
        r += 1

    return max_length
    



printx(maxTurbulenceSize(arr = [9,4,2,10,7,8,8,1,9])) # 5
printx(maxTurbulenceSize(arr = [4,8,12,16])) # 2
printx(maxTurbulenceSize(arr = [100])) # 1