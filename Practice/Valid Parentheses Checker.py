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
        if b in set(brackets.keys()):
            stack.append(b)
        else:
            if not stack or brackets[stack.pop()] != b:
                return False

    return len(stack) == 0, s, stack



print(check("(((()))("))
# Expected: False

print(check("[(])"))
# Expected: False

print(check("]"))
# Expected: False

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
