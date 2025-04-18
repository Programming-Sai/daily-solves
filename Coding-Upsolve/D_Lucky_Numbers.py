def luckiest_number(l, r):
    for i in range(r, l - 1, -1):  # Start from the largest number
        digits = [int(d) for d in str(i)]
        luckiness = max(digits) - min(digits)
        if luckiness == 9:  # Maximum possible, stop early
            return i
    return max(range(l, r+1), key=lambda x: max(map(int, str(x))) - min(map(int, str(x))))

t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    print(luckiest_number(l, r))
