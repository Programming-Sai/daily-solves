from fprintx import printx

def check(s):
    n = len(s)
    s_count = 0
    l = r = 0
    while r < n:
        while l < n and s[r] != s[l]:
            s_count -= 1
            l += 1
            
        s_count+=1
        if s_count >= 7:
            print('YES')
            return
        
        r += 1
    print('NO')
    return 



s = list(input())
check(s)