t = int(input())
for _ in range(t):
    n = int(input())
    plays = list(map(int, input().split()))
    prev_plays = 0
    num_plays = 0
    for play in plays:
        if play >= prev_plays:
            num_plays += play - prev_plays
        prev_plays = play
    print(num_plays)

