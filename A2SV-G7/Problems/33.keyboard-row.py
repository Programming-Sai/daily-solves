def findWords(words):
    check = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
    result = []
    for word in words:
        for c in check:
            if set(word.lower()).issubset(c):
                result.append("".join(word))

    return result