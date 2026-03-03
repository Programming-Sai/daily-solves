from typing import List

def findRelativeRanks(score: List[int]) -> List[str]:
    map = {}
    sorted_score = sorted(score, reverse=True)
    res = []
    for score_, rank in zip(sorted_score[:3], ["Gold Medal","Silver Medal","Bronze Medal"]):
        map[score_] = rank
    for idx, score_ in enumerate(sorted_score[3:]):
        map[score_] = str(idx+4)
    for s in score:
        res.append(map[s])
    return res