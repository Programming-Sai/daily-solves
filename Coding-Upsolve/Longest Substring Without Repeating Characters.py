from fprintx import printx

def lengthOfLongestSubstring(s):
    window_count = [0] *26
    n = len(s)
    # for i in range(s):
        # window_count[(ord(i) - ord('a'))] += 1

    l = r = 0
    longest = 0
    while r < n:
        printx(window_count, s[l], longest, l, r, widths=[5])
        # window_count[(ord(s[r]) - ord('a'))] += 1
        longest = max(longest, (r-l)+1)
        while window_count[(ord(s[r]) - ord('a'))] > 1:
            window_count[(ord(s[l]) - ord('a'))] -= 1
            l += 1
        window_count[(ord(s[r]) - ord('a'))] += 1
        
        r += 1
    return longest
        
        


print(lengthOfLongestSubstring(s = "abcabcbb"))
# print(lengthOfLongestSubstring(s = "pwwkew"))
# print(lengthOfLongestSubstring(s = "bbbbb"))