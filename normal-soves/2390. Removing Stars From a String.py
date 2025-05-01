from fprintx import printx



def removeStars(s: str) -> str:
    stack = []
    for x in s:
        if x == '*': 
            if  stack:
                stack.pop()
        else:
            stack.append(x)
    return "".join(stack)


print(removeStars(s = "leet**cod*e"))
print(removeStars(s = "erase*****"))


