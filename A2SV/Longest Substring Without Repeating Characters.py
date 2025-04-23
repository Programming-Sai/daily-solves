from collections import defaultdict
from fprintx import printx




def lengthOfLongestSubstring(s):
    # max_length = float('-inf')
    max_length = 0
    # max_length = len(s)
    counter = defaultdict(int)
   
    l = r = 0
    while r < len(s):
        counter[s[r]] += 1       

        # printx(l, r, counter, widths=[5])
        while counter[s[r]] > 1:
            counter[s[l]]-= 1
            l += 1
        
        max_length = max(max_length, (( r - l ) + 1))
        r += 1
    return max_length


print(lengthOfLongestSubstring(s = "abcabcbb"))
print(lengthOfLongestSubstring(s = "pwwkew"))
print(lengthOfLongestSubstring(s = "bbbbb"))
print(lengthOfLongestSubstring(s = ""))
print(lengthOfLongestSubstring(s = " "))


