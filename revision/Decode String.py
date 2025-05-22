from fprintx import printx


def decodeString(s: str) -> str:
    n = len(s)
    current_string = num = ""
    str_stack, int_stack = [], []
    for i in range(n):
        if s[i].isdigit():
            num += s[i]
        elif s[i] == '[':
            int_stack.append(int(num))
            str_stack.append(current_string)
            num = current_string = ""
        elif s[i] == ']':
            prev =  str_stack.pop()
            count = int_stack.pop()
            current_string = prev + (current_string * count)
        else:
            current_string += s[i]
    return current_string
            
            



print(decodeString(s = "3[a]2[bc]"))
print(decodeString(s = "3[a2[c]]"))
print(decodeString(s = "2[abc]3[cd]ef"))
print(decodeString(s = "10[a]"))
print(decodeString(s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
print(decodeString(s = "abc3[cd]xyz"))

