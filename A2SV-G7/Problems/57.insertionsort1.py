def insertionSort1(n, arr):
    target = arr[-1]
    
    for i in range(n-2, -1, -1):
        if arr[i] > target:
            arr[i+1] = arr[i]
            print(" ".join([str(i) for i in arr]))
        else:
            arr[i+1] = target
            print(" ".join([str(i) for i in arr]))
            return 
    arr[0] = target
    print(" ".join([str(i) for i in arr]))
            
     