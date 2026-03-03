# - pick 2 numbers... sliding of 2 items each
# - if check if x is in range a and break
# - if it is replace both a and b (collapse them) into a number closer to x or x itself
# - if not move on.

def soln(n, a, x):
    min_a = min(a)
    max_a = max(a)
    return "YES" if x in range(min_a, max_a) else "NO"



T=int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    print(soln(n, a, x))