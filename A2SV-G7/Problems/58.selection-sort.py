def selectionSort(arr):
    start = 0
    for i in range(len(arr)):
        smallest, s_idx = float("inf"), -1
        for j in range(start, len(arr)):
            if arr[j] < smallest:
                smallest = arr[j]
                s_idx = j
        arr[s_idx], arr[start] = arr[start], arr[s_idx]
        start += 1
        