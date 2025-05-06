
from fprintx import printx



def check(n, a, b):
    winner = None
    turn = 'a'
    while True:
        if turn == 'a':
            if a > b and (a-1) > 0 and (a-1) != b:
                a -= 1
            elif a < b and (a + 1) < n+1 and (a+1) != b:
                a += 1
        
        turn  = 'b'
        if turn  == 'b':
            if b > a and (b-1) > 0 and (b-1) != a:
                b -= 1
            elif b < a and (b + 1) < n+1 and (b+1) != a:
                b += 1
        turn  = 'a'

        if 0 < a < b or b < a < n+1:
            winner = 'b'
            return 'NO'
        elif 0 < b < a or a < b < n+1:
            winner = 'a'
            return 'YES'
        

n, a, b = 2, 1, 2
print(check(n, a, b))




# t=int(input())
# for _ in range(t):
    # n, a, b = map(int, input().split())
    # print(check(n, a, b))