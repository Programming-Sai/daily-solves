def restoreString(s, indices):
    res = [None for _ in range(len(indices))]
    for i in range(len(s)):
        res[indices[i]] = s[i]
    return "".join(res) 