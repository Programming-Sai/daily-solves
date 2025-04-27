from fprintx import printx

import math

def check(x):
    possibilities = set(range(1, math.ceil(x ** ((1/3)))+1))
    # print(5779 in possibilities)
    for i in possibilities:
        # j = x-i**3 

        # print(j, (j)**(1/3)) if i == 5779 else ""
        # printx(i, math.floor((x-(i**3))**(1/3)), (x-(i**3))**(1/3), (x-i**3) ** (1/3), math.floor(x ** ((1/3))), possibilities if len(possibilities) < 10 else "") if i == 5779 else ""
        if x - (i ** 3) < 0:
            continue
        if math.ceil((x-(i**3))**(1/3)) in possibilities and ((i**3) +  (math.ceil((x-(i**3))**(1/3)))**3 == x):
            print('YES')
            return
    print("NO")

# check(34)
# check(35)
# check(16)
# check(703657519796)


t = int(input())
for _ in range(t):
    x = int(input())
    check(x)