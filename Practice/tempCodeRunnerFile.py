from fprintx import printx


def check(temps):
    stack = []
    result = [0] * len(temps)
    for i in range(len(temps)):
        while stack and temps[stack[-1]] <= temps[i]:
            p = stack.pop()
            result[p] = i - p
        stack.append(i)
    return result


print(check([73, 74, 75, 71, 69, 72, 76, 73]))
# Expected: [1, 1, 4, 2, 1, 1, 0, 0]

print(check([30, 40, 50, 60]))
# Expected: [1, 1, 1, 0]

print(check([30, 60, 90]))
# Expected: [1, 1, 0]

print(check([90, 80, 70, 60]))
# Expected: [0, 0, 0, 0]
