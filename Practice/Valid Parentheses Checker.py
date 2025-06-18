def check(s: str) -> bool:
    """
    Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', 
    determine if the input string is valid.

    A string is valid if:
    1. Open brackets are closed by the same type.
    2. Open brackets are closed in the correct order.
    """
    if s == "": return True, s
    brackets = {'(':')', '{':'}', '[':']'}
    closers = {']', '}', ')'}
    stack = []

    for b in s:
        if stack and stack[-1] not in closers:
            if b == brackets[stack[-1]]:
                stack.pop()
        stack.append(b)

    return not (len(stack) == len(s)), s, stack




print(check("()"))  
# Expected: True

print(check("()[]{}"))  
# Expected: True

print(check("(]"))  
# Expected: False

print(check(""))  
# Expected: True  
# Empty string is trivially valid

print(check("((((((((("))  
# Expected: False  
# No closing brackets

print(check("([{}])"))  
# Expected: True  
# Perfectly nested
