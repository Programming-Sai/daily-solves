from fprintx import printx


def check(n):
    m=(2 * n) + 1
    j=0
    for i in range(m):
        top = ([x  for x in range(i+1)] + [x  for x in range(i-1, -1, -1)])
        bottom = ([x for x in range((n-j))] + [x for x in range(((n-j)-2), -1, -1)])
        if i <= n:
            print("  " * (((n - i) if i < n else (i - n))), end="")
            print(*top)
        else:
            print("  " * (((n - i) if i < n else (i - n))), end="")
            print(*bottom)


        if i > n:
            j += 1

# n=int(input())
# check(n)

for i in range(1, 10):
    check(i)

# n=9
# check(n)

