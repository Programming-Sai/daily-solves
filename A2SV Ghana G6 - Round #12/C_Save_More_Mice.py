from fprintx import printx


def check(n, k, stack):
    stack.sort()
    cat = result = 0

    while stack[-1] > cat:
        if stack:
            print(stack, cat)
            if stack[-1] >= n:
                stack.pop()
                result+=1
        if stack:
            stack[-1]+=1
            cat+=1
        if not stack:break
    return result



t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    stack = list(map(int, input().split()))
    print(check(n, k, stack))