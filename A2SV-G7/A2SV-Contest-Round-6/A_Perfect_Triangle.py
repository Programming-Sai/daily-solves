
def soln(decs, n):
    l, r, min_moves, decs = 0, 2, float("inf"), sorted(decs)
    while r < n:
        min_moves = min(min_moves, ((decs[l+1] - decs[l]) + (decs[r] - decs[l+1])))
        l += 1
        r += 1
    return min_moves if min_moves != float("inf") else 0



t = int(input())
for _ in range(t):
    n = int(input())
    decs = list(map(int, input().split()))
    print(soln(decs, n))