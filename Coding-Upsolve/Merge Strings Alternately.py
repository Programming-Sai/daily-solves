def mergeAlternately(word1, word2):
        w1, w2 = 1, 0
        res=word1[0]
        state=1
        while w1 < len(word1) and w2 < len(word2):
            # print(res, w1, w2, state)
            if state % 2:
                res += word2[w2]
                w2 += 1
            else:
                res += word1[w1]
                w1 += 1
            state += 1
        if len(word1) > len(word2):
            res += word1[w1:]
        elif len(word2) > len(word1):
            res += word2[w2:]
        else:
            res += word2[w2:]
        return res



_ = int(input())
for i in range(_):
    word1 = input()
    word2 = input()

    print(mergeAlternately(word1, word2))