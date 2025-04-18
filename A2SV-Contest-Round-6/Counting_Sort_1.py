
def countingSort(arr):
    output = [0] * 100
    for item in arr:
        output[item] += 1
    
    result = ''
    for item in output:
        result += " " + str(item)
    print(result)
    return result
    # return output


n=int(input())
arr = list(map(int, input().split()))
countingSort(arr)