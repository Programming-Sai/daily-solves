from fprintx import printx

def check(s: str) -> str:
    """
    Given an encoded string `s`, return its decoded version.

    Encoding follows the pattern k[encoded_string], where the encoded_string inside the 
    square brackets is repeated exactly k times.

    Assume input is always valid.
    """
    dig_stk, str_stk = [], []
    curr, num = "", 0
    for st in s:
        # printx(curr, type(curr), num, st, str_stk, dig_stk)
        if st.isdigit():
            num = num * 10 + int(st)
        elif st == "[":
            str_stk.append(curr)
            dig_stk.append(int(num))
            curr, num = "", 0
        elif st == ']':
            repeater = dig_stk.pop()
            prev_str = str_stk.pop()
            curr = prev_str + curr * repeater
        else:
            curr += st
    return curr



print(check("3[a]2[bc]"))  
# Expected: "aaabcbc"

print(check("3[a2[c]]"))  
# Expected: "accaccacc"

print(check("2[abc]3[cd]ef"))  
# Expected: "abcabccdcdcdef"

print(check(""))  
# Expected: "" — Nothing to decode

print(check("10[a]"))  
# Expected: "aaaaaaaaaa"

print(check("xyz"))  
# Expected: "xyz" — No encoding at all
