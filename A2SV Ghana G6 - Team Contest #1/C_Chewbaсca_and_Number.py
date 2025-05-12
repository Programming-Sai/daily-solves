from fprintx import printx





def check(x):
    v = set(x)
    if len(v) == 1 and '9' in v:
        return x    
    return int("".join([str(9 - int(i)) if 9 - int(i) < int(i) else str(int(i)) for i in x]))


print(check((input())))


