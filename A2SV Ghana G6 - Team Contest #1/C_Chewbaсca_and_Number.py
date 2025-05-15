from fprintx import printx





def check(x):
    return int("".join([str(int(x[i]))   if (i == 0 and x[i] == '9') or int(x[i]) < 5  else str(9 - int(x[i])) for i in range(len(x))]))


print(check((input())))


