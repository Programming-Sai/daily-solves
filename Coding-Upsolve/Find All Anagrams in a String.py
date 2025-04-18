from fprintx import printx


def findAnagrams(s, p):
    window_counter = [0] * 26
    target_counter = [0] * 26
    m = len(s)
    n = len(p)
    result = []
    for i in p:
        target_counter[ord(i) - ord('a')] += 1

    for i in range(n):
        window_counter[ord(s[i]) - ord('a')] += 1

    

    l = 1
    r = l + n - 1
    while r < m:        
        # printx(target_counter, window_counter, l, r, s[l-1], s[r], s[l:r], result, widths=[5])

        if window_counter == target_counter:
            result.append(l-1)
            # printx('match', l, r)
            
        window_counter[ord(s[l - 1]) - ord('a')] -= 1
        window_counter[ord(s[r]) - ord('a')] += 1

        l += 1
        r += 1
    if window_counter == target_counter:
            result.append(l-1)
            # print('match', l, r)




    return (result)


print(findAnagrams(s = "cbaebabacd", p = "abc"))
print(findAnagrams(s = "abab", p = "ab"))