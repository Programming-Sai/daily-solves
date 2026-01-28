def swap_case(s):
    res = ""
    for x in s:
        if x.isupper():
            res += x.lower()
        else:
            res += x.upper()
    return res
            
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)