from collections import defaultdict, deque
from fprintx import printx


def check(n, k, a):
    freq = defaultdict(int)
    window = deque()
    window_set = set()
    l = r = max_len = 0
    


n, k = list(map(int, input().slpit()))
a = list(map(int, input().split()))
print(*check(n, k, a))