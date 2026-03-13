n = int(input())
cards = list(map(int, input().split()))
l, r, s_score, d_score, s_turn = 0, n - 1, 0, 0, True
while l <= r:
    if s_turn:
        if cards[l] > cards[r]:
            s_score += cards[l]
            l += 1
        else:
            s_score += cards[r]
            r -= 1 
    else:
        if cards[l] > cards[r]:
            d_score += cards[l]
            l += 1
        else:
            d_score += cards[r]
            r -= 1 
    s_turn = not s_turn
print(s_score, d_score)