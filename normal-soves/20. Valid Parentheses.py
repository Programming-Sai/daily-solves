from fprintx import printx


def isValid(s: str) -> bool:
    opening_set = {'(', '[', '{'}
    closing_set = {')', ']', '}'}
    opening = {')':'(', '}':'{', ']':'['}
    stack=[]
    for x in s:
        if x in opening_set:
            stack.append(x)
            continue
        if x in closing_set and stack[-1] == opening[x] and stack:
            stack.pop()
    return not stack




# print(isValid(s = "()"))
# print(isValid(s = "()[]{}"))
# print(isValid(s = "(]"))
print(isValid(s = "([])"))