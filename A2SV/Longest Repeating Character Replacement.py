from fprintx import printx



def characterReplacement(s, k):
    n = len(s)
    counter = [0] * 26
    


    l = r = max_length = max_freq = window_length = 0
    while r < n:
        # if r+1<n :printx(counter[ ord(s[r+1]) - ord('A') ], l, r, max_item_count, max_length, ((r - l) + 1), overflow_index, m, k, s, widths=[6])
        counter[ ord(s[r]) - ord('A') ] += 1
        max_freq = max(max_freq, counter[ ord(s[r]) - ord('A') ])
        window_length = r-l+1
        if window_length - max_freq > k:
            counter[ ord(s[l]) - ord('A') ] -= 1
            l += 1
        max_length = max(max_length, r-l+1)
        r += 1
    return max_length



    # print(counter, max_item_count)
    



print(characterReplacement(s = "ABAB", k = 2))
print(characterReplacement(s = "AABABBA", k = 1))