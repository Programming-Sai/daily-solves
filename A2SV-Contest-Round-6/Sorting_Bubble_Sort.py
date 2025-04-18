from fprintx import printx


def insertionSort1(n, arr):
    target = arr.pop()
    for i in range(n-2, -1, -1):
        # printx(target, arr[i], i, styles=['bold'])
        if arr[i] <= target:
            # print(arr)
            arr.insert(i+1, target)
            for j in arr:
                print(j, end=" ")
            print()
            break
        else:
            arr.insert(i, arr[i])
            for j in arr:
                print(j, end=" ")
            print()
            arr.pop(i)
    if target < arr[0]:
        arr.insert(0, target)
        for j in arr:
            print(j, end=" ")
        print()


# def insertionSort1(n, arr):
#     # Store the target value that needs to be inserted in sorted order.
#     target = arr[-1]
    
#     # Start from the element just before the target.
#     i = n - 2
    
#     # Shift elements to the right until finding the correct spot.
#     while i >= 0 and arr[i] > target:
#         arr[i+1] = arr[i]   # Shift the element to the right.
#         # Print the array after each shift.
#         print(" ".join(map(str, arr)))
#         i -= 1
    
#     # Insert the target in its correct position.
#     arr[i+1] = target
#     # Print the final state of the array.
#     print(" ".join(map(str, arr)))


# Example usage:
n = 10
arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
insertionSort1(n, arr)



# # Example usage:
# n = 5
# arr = [2, 4, 6, 8, 3]
# insertionSort1(n, arr)
