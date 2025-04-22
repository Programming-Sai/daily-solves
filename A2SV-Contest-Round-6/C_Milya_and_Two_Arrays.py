

from fprintx import printx
    


def check(a, b, n):
    set_a = set(a)
    set_b = set(b)
    set_c = set()
    for i in set_a:
        for j in set_b:
            # printx(set_a, set_b, set_c)
            set_c.add(i + j)
            if len(set_c) >= 3:
                print('YES')
                return 
    print('NO')





t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    check(a, b, n)
           

