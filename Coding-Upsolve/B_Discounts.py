
def get_prefix_sum(arr):
    prefix_sum = [0] * (len(arr)+1)
    for i in range(len(arr)):
        if (i + 1) > len(arr):
            break
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]
    return (prefix_sum)


 
n=int(input())
a=list(map(int, input().split()))
m=int(input())
q=list(map(int, input().split()))
a.sort() 
prefix_sum = get_prefix_sum(a)[n]
for x in q:
    print(prefix_sum - a[n - x])
 