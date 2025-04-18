from fprintx import printx



def check(n, s):
    sorted_s = sorted(s, reverse=True)
    output = []
    for i in range(n):
        # printx(i, s[i], ( sorted_s[0] if s[i] != sorted_s[0] else sorted_s[1]), widths=[10])
        output.append(s[i] - ( sorted_s[0] if s[i] != sorted_s[0] else sorted_s[1]) )
    # printx(*output, widths=[1])
    for item in output:
        print(item, end=' ')
    print()


t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    check(n, s)
n= 4


s=[4, 7, 3, 5]

n=5
s=[1, 2, 3, 4, 5]
# check(n, s)


