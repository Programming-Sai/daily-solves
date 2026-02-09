
def sol(strs):
    if not strs:
        return ""
    shortest_str = min(strs, key=lambda x:len(x))
    strs.remove(shortest_str)
    for i in range(len(shortest_str)):
        for str_ in strs:
            if shortest_str[i] != str_[i]:
                return shortest_str[:i]
    return shortest_str

