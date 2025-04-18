def  check(a, b, c, d):
    red_range = set(range(*sort_swap(a, b)))
    blue_range = set(range(*sort_swap(c, d)))

    if blue_range.issubset(red_range) or red_range.issubset(blue_range): return 'NO'

    for i in blue_range:
        if i in red_range:
            return ("YES")
        
    return ("NO")

def sort_swap(x, y):
    if x > y:
        return [y, x+1]
    else:
        return [x, y+1]
    


t=int(input())
for _ in range(t):
    a, b, c, d = list(map(int, input().split()))
    print(check(a, b, c, d))
    






    

# a, b, c, d = [2, 9, 10, 6]
# a, b, c, d = [3, 8, 9, 1]

# print(check(a, b, c, d))


