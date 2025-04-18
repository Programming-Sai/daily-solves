from fprintx import printx


def pancakeSort(arr):
    result = []
    max_item = n = len(arr)
    c = 0
    for i in range(len(arr)):
        # print(arr, "I block check")
        if is_sorted(arr):
            break
        print(" i", i)
        for j in range(len(arr)-i):
            print("     j", j)
            if arr[j] == max_item:
                arr = arr[:j] + arr[j:n-i][::-1]  + arr[n-i:]
                max_item -= 1                
                print(arr, n-i)
                result.append(j+1)
                c += 1
                break
    return result, c


# def pancakeSort(arr):
#     result = []
#     for x in range(len(arr), 1, -1):
#         i = arr.index(x)
#         result.extend([i + 1, x])
#         arr = arr[:i:-1] + arr[:i]
#     return result


def is_sorted(self, arr):
    # is_arr_sorted = False
    # print("Sorting")
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True



def pancakeSort(self, arr):
    i, j, n = 0, 0, len(arr)
    result = []
    max_item = n
    for _ in range(n):
        if self.is_sorted(arr):
            break
        for i in range(n-j):
            # print(i, j)
            if arr[i] == max_item:
                result.append(i+1)
                arr[:i+1] = arr[:i+1][::-1]
                # printx(arr, i, j, arr[:i+1], arr[:n-j], n, n-j, max_item, result, "Before")
                arr[:n-j] = arr[:n-j][::-1]
                # j+=1
                max_item -= 1
                j += 1
                # printx(arr, i, j, arr[:i+1], arr[:n-j], n, n-j, max_item, result, "After")
    return result



def pancakeSort(arr):
    max_item = n = len(arr)
    result = []

    while max_item > 1:

        max_index = -1
        for i in range(n):
            if arr[i] == max_item:
                max_index = i
                break
        
        if max_index != max_item -1:
            if max_index != 0:
                arr[:max_index+1] = arr[:max_index+1][::-1]
                result.append(max_index + 1)

            arr[:max_item] = arr[:max_item][::-1]
            result.append(max_item)

        max_item -= 1
    return result

            






print(pancakeSort(arr = [3,2,4,1]))
# print(pancakeSort(arr = [1, 2, 3]))
# print(pancakeSort(arr = [5, 3, 2, 7, 6, 4, 1]))
# print(pancakeSort(arr = [7, 6, 5, 4, 3, 2, 1][::-1]))
# print(pancakeSort(arr = [1, 7, 2, 6, 3, 5, 4]))
