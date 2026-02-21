from collections import defaultdict
def queryResults(limit, queries):
    bc={}
    cf=defaultdict(int)
    res=[]
    for b, c in queries:
        if b in bc:
            cf[bc[b]] -= 1
            if cf[bc[b]] <= 0: del cf[bc[b]]
        cf[c] += 1
        bc[b] = c
        res.append(len(cf))
    return res