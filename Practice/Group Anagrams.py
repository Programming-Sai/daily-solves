from fprintx import printx
from typing import List
from collections import Counter, defaultdict

def check(strs: List[str]) -> List[List[str]]:
    """
    Given a list of strings, group anagrams together.

    Output can be in any order.
    """
    # Create Counter List for all
    # counter_list = [Counter(_str) for _str in strs]
    # counter_set = []
    # for count in counter_list:
    #     if count in counter_set:continue
    #     counter_set.append(count)
    # # print(counter_list, "\n", counter_set)
    
    # result = []
    # for count in counter_set:
    #     inter = []
    #     for _str in strs:
    #         if Counter(_str) == count:
    #             inter.append(_str)
    #     result.append(inter)
    # return result

    segments = defaultdict(list)
    for _str in strs:
        segments[tuple(sorted(_str))].append(_str)
    return list(segments.values())


print(check(["eat","tea","tan","ate","nat","bat"]))
# Expected: [["eat","tea","ate"],["tan","nat"],["bat"]]

print(check(["a"]))  
# Expected: [["a"]]

print(check([""]))  
# Expected: [[""]]

print(check(["",""]))  
# Expected: [["",""]] — two empty strings are anagrams

print(check(["ab","ba","abc","cab","bac"]))  
# Expected: [['ab','ba'], ['abc','cab','bac']]
