

def imageSmoother(img):
    m, n = len(img), len(img[0])
    result = [[None for _ in range(n)] for _ in range(m)]
    def getAvg(cx, cy):
        s, c, offsets = img[cx][cy], 1, [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        for dx, dy in offsets:
            if 0 <= (cx + dx) < m and 0 <= (cy + dy) < n:
                s += img[cx + dx][cy + dy]
                c += 1
        result[cx][cy] = s // c

    for r in range(m):
        for c in range(n):
            getAvg(r, c)
    return result


