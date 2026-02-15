from collections import Counter

def areAlmostEqual(s1: str, s2: str) -> bool:
    diff_pos_count, n = 0, len(s1)
    for i in range(n):
        if s1[i] != s2[i]:
            diff_pos_count += 1
    return Counter(s1) == Counter(s2) and diff_pos_count in [0, 2]