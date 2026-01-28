import math
n, k = map(int, input().split())
count_of_odd = math.ceil(n/2)
if k <= count_of_odd:
    print((2*k) - 1)
else:
    print(2*(k - count_of_odd))