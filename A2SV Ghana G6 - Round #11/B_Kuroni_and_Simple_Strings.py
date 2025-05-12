from fprintx import printx



def check(s):
    l = 0
    r = len(s)-1
    result =[]
    while l < r:
        while l < r and s[l] != '(':
            l += 1
        while l < r and s[r] != ')':
            r -= 1

        if s[l] == '(' and s[r] == ')':
            result.extend([l+1, r+1])
        l += 1
        r -= 1
    print(int(bool(result)))
    if result:
        print(len(result))
        print(*sorted(result))


check(input())