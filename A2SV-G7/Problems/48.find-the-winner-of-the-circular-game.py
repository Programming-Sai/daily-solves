def findTheWinner(n, k):
    players=[i+1 for i in range(n)]
    current_idx = 0
    while len(players) > 1:
        current_idx = (current_idx + k - 1) % len(players)
        players.pop(current_idx)
    return players[0]
    