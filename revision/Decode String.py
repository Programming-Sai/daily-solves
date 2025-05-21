from fprintx import printx


def decodeString(s: str) -> str:
    n = len(s)
    result = []
    num_stack = []
    str_stack = []
    i = n-1
    while i > 0:
        if s[i] == ']':
            j = i
            while True:
                if s[j] == '[':
                    break
                # if s[j] == ']':
                    # decodeString()
                num_stack.append(s[j])
            i = j
            
            



print(decodeString(s = "3[a]2[bc]"))
# print(decodeString(s = "3[a2[c]]"))
# print(decodeString(s = "2[abc]3[cd]ef"))

