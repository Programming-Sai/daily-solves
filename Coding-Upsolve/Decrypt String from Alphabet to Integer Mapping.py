def freqAlphabets(s):
    alphabets = {i: chr(i+96) for i in range(1, 27)}
    nums = []
    i=len(s)-1
    while i >= 0:
        if s[i] == '#':
            nums.append((    chr (int(s[i-2]+s[i-1]) + 96)       ))
            i -= 3
            continue
        nums.append(     chr(int(s[i]) + 96)      )
        i -= 1
    nums.reverse()
    return "".join(nums)

print(freqAlphabets("1326#"))
print(freqAlphabets("10#11#12"))
