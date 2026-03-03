# - each tries to find a max >= mx. if one is able to then thier score increases

# def soln(n, a):
#     d_score, z_score, mx, d_turn, maxes = 0, 0, 0, True, sorted([(num, i) for i, num in enumerate(a)], key=lambda x: x[0], reverse=False)
#     for _ in a:
#         current_max, current_max_idx = maxes[-1]
#         maxes.pop()
#         if d_turn:
#             if current_max >= mx: d_score += 1
#         else:
#             if current_max >= mx: z_score += 1

#         # print(a, d_score, z_score, mx, current_max)
        
#         mx = max(current_max, mx)   
#         a[current_max_idx] = 0
#         d_turn = not d_turn
#     return "YES" if d_score > z_score else "NO"


# def soln(n, a):
#     return "YES" if sum(a) % 2 else "NO"


def soln(n, a):
    mx = 0
    turn = True  
    a_sorted = sorted(a, reverse=True)
    
    for i in range(n):
        if a_sorted[i] >= mx:
            mx = a_sorted[i]
            a_sorted[i] = 0
            turn = not turn
        else:
            return "NO" if turn else "YES"
    
    return "YES" if not turn else "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(soln(n, a))