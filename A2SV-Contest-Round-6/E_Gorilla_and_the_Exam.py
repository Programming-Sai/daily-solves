# Create coutner for the arr
# create an arr of the coutns and sort 
# MAke sure that each value is < the current k
# k gets reducsed each time

from fprintx import printx


from collections import Counter

def check(n, k, a):
    if len(a) == 1:
        return 1
    counter = Counter(a)
    counter_arr = sorted(list(counter.values()))
    # printx(counter, counter_arr, k, "Before", alignments=['>'])
    j = 0
    # current_count = 
    for i in range(len(counter_arr)):
        if counter_arr[i] <= k:
            k -= counter_arr[i]
        else:
            return len(counter_arr) - j
        j += 1
    
    return max(1, len(counter_arr) - j )




def check2(n, k, a):
    a.sort()
    counter = [1]
    for i in range(n-1):
        if a[i] == a[i + 1]:
            counter[-1] += 1
        else:
            counter.append(1)
    # print(counter)

    counter.sort()
    j = 0
    # current_count = 
    for i in range(len(counter)):
        if counter[i] <= k:
            k -= counter[i]
        else:
            return len(counter) - j
        j += 1
    
    return max(1, len(counter) - j )



    

    # printx(counter, counter_arr, k, "After", alignments=['>'])





n, k, a = 11, 4, [3, 2, 1, 4, 4, 3, 4, 2, 1, 3, 3,]
# n, k, a = 1 ,0, [48843]
# n, k, a = 7, 0, [4, 7, 1, 3, 2, 4, 1]
# n, k, a = 3, 1, [2, 3, 2]
# print(check2(n, k, a))

t=int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print(check2(n, k, a))



