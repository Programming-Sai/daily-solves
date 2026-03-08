"""
so lets take a look at my intuition for this.

we could sort the array. this is because in order to get i and j to be < 1 the best scanrio would be if they are together. 

now after sorting we move from index 1 (skipping 0) then we check if abs(a[i] - a[i-1] <= 1) now if that is the case we take the smaller of the 2 and then send thatval to None

next we would keep this up till the ned of the arr, ignoring... ideally ignoring all null vals. using the remove mthod would be 0(n)...

say we did that and removed the item so a for loop would not cut it, so a while loop. now we would also be updatingthe n as we go. now if at some point n == 1 or even when we end the loop

and then we can come back and check if n == 1. if that is the case then yes, else no.

----

Turns out you just need to loop through, and check for gaps. where there are any > 1, red flag, end with a no.

"""

t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))
    for i in range(1, n):
        # print("Debug: ", a[i] - a[i-1]," | ", a[i], a[i-1])
        if abs(a[i] - a[i-1]) > 1:
            print("NO")
            break
    else:
        print("YES")
