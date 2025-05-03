from fprintx import printx

from collections import Counter, defaultdict


def check(n, a):
    # counter = Counter(a)
    counter = defaultdict(int)
    # printx(counter)
    for count in a:
        counter[count] += 1
        if counter[count] >= 3:
            return count
    return -1


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(check(n, a))

