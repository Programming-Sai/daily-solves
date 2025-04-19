

'''
DONE
'''

def check(n):
    timur = n[0]
    n.sort()
    timur_index = 0
    for i in range(len(n)):
        if n[i] == timur:
            timur_index = i
    return len(n) - timur_index - 1


t = int(input())
for _ in range(t):
    n = list(map(int, input().split()))
    print(check(n))