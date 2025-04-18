def findTheWinner(n, k):
    players=[i for i in range(1, n+1)]
    # print(players)
    i=0
    while len(players) > 1:
        i = (i + k - 1) % len(players)
        players.pop(i)
    return players[0]

# print(findTheWinner(n = 5, k = 2))
# print(findTheWinner(n = 6, k = 5))
