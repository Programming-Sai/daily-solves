from collections import Counter

def commonChars(words):
    freq = Counter(words[0])
    for i in range(1, len(words)):
        word_count = Counter(words[i])
        for k, v in freq.items():
            freq[k] = min(v, word_count[k])
    res = []
    for c in freq:
        for i in range(freq[c]):
            res.append(c)
    return res