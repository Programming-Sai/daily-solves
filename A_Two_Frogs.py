
from fprintx import printx



def check(n, a, b):
    winner = None
    turn = 'a'
    while True:
        print(['a' if i == a else 'b' if i == b else "_" for i in range(1, n+1)])


        if turn == 'a':
            if (a > b and (a-1) > 0 and (a-1) != b) or (a+1 == b and a-1 > 0):
                a -= 1
            elif (a < b and (a + 1) < n+1 and (a+1) != b) or (a-1 == b and a+1 < n+1):
                a += 1


        print(['a' if i == a else 'b' if i == b else "_" for i in range(1, n+1)])
        turn  = 'b'


        if turn  == 'b':
            if (b > a and (b-1) > 0 and (b-1) != a) or (b+1 == a and b-1 > 0):
                b -= 1
            if( b < a and (b + 1) < n+1 and (b+1) != a) or (b-1 == a and b+1 < n+1):
                b += 1



        print(['a' if i == a else 'b' if i == b else "_" for i in range(1, n+1)])
        turn  = 'a'

        if (0 < a < b or b < a < n+1) and (a == b+1 or a == b-1):
            winner = 'b'
            print(0, a, b, n+1)
            return 'NO'
        elif (0 < b < a or a < b < n+1) and (b == a+1 or b == a-1):
            winner = 'a'
            print(0, a, b, n+1)
            return 'YES'
        

# n, a, b = 2, 1, 2
n, a, b = 5, 2, 4
print(check(n, a, b))




# t=int(input())
# for _ in range(t):
    # n, a, b = map(int, input().split())
    # print(check(n, a, b))