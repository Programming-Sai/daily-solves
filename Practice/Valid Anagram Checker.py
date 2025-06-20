from fprintx import printx
from collections import Counter



def check(s: str, t: str) -> bool:
    """
    Given two strings `s` and `t`, return True if `t` is an anagram of `s`, 
    and False otherwise.

    An anagram is formed by rearranging the letters of a word using all original letters exactly once.
    """
    s_count = Counter(s)
    t_count = Counter(t)
    printx(s_count, t_count, s, t, widths=[7])
    return s_count == t_count



print(check("anagram", "nagaram"))  
# Expected: True

print(check("rat", "car"))  
# Expected: False

print(check("aabbcc", "abcabc"))  
# Expected: True

print(check("", ""))  
# Expected: True

print(check("a", "aa"))  
# Expected: False

print(check("abc", "cba "))  
# Expected: False — Space included, not same chars
