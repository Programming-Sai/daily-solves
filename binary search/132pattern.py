def pattern(num):
    n = len(num)
    left = [None] * n
    right = [None] * n
    stack = []
    for i in range(n-1, -1, -1):
        while stack and num[i] > stack[-1]:
            left[i] = stack.pop()
        stack.append(num[i])
    stack.clear()
    for i in range(n):
        while stack and num[i] > stack[-1]:
            right[i] = stack.pop()
        stack.append(num[i])
        if left[i] and right[i]:
            return True
    return False

    for i in range(n):
        if left[i] and right[i]:
            return True
    return False

print(pattern([1, 2, 3, 4]))
print(pattern([-1, 3, 2, 0]))
print(pattern([1, 0, 1, -4, -3]))