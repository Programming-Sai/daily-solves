from collections import defaultdict

def numberOfBoomerangs(points):
    count = 0
    for point_i in points:
        map = defaultdict(int)
        for point_j in points:
            if point_i == point_j: continue
            map[(((point_j[0] - point_i[0])**2) + ((point_j[1] - point_i[1])**2))]  += 1
        for k, v in map.items():
            count += (map[k] * (map[k] - 1))
        del map
    return count
