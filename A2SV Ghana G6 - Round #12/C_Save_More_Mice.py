from fprintx import printx


def check(n, k, stack):
    unique_positions = sorted(set(stack), reverse=True)
    
    saved = 0
    total_distance = 0
    
    for pos in unique_positions:
        dist = n - pos
        if total_distance + dist < n:
            saved += 1
            total_distance += dist
        else:
            break
    return saved



t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    stack = list(map(int, input().split()))
    print(check(n, k, stack))