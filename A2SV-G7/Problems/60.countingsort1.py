def countingSort(arr):
    counter = [0 for _ in range(100)]
    for ar in arr:
        counter[ar] += 1
    return counter


print(countingSort([5, 2, 4, 10, 5, 7]))