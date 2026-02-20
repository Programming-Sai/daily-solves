def escapeGhosts(ghosts, target):
    my_moves_count = abs(target[0]-0)+abs(target[1]-0)
    for gx, gy in ghosts:
        ghosts_moves_count = abs(target[0]-gx)+abs(target[1]-gy)
        # print(my_moves_count, ghosts_moves_count)
        if ghosts_moves_count <= my_moves_count:
            return False
    return True