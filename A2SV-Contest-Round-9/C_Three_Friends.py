'''
Solution is to minimise a and c to that they are closer to b
'''


def check(a, b, c):
    return abs((a+(1 if a < b else 0)) - b) + abs(b - (c-(1 if c > b else 0))) + abs((a+(1 if a < b else 0)) - (c-(1 if c > b else 0)))


t = int(input())
for _ in range(t):
    a, b, c = list(map(int, input().split()))
    print(check(a, b, c))