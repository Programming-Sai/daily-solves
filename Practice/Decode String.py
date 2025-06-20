

def check(s: str) -> str:
    """
    Given an encoded string `s`, return its decoded version.

    Encoding follows the pattern k[encoded_string], where the encoded_string inside the 
    square brackets is repeated exactly k times.

    Assume input is always valid.
    """
    num_stack, str_stack = [], []
    curr, num = "", 0
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == "[":
            str_stack.append(curr)
            num_stack.append(num)
            curr = ""
            num = 0
        elif ch == "]":
            repeat = num_stack.pop()
            prev = str_stack.pop()
            curr = prev + curr * repeat
        else:
            curr += ch





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
