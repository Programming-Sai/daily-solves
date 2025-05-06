from fprintx import printx



def add(a, b):
    print(a, "+", b)
    return a+b
def sub(a, b):
    print(a, "-", b)
    return int(a)-int(b)
def multipy(a, b):
    print(a, "*", b)
    return a*b
def div(a, b):
    print(a, "/", b)
    return int(a / b) if a * b > 0 else -(abs(a) // abs(b))
def evalRPN(tokens):
    stack = []
    opeartions_set = {'+', '-', '/', '*'}
    operations = {
        '+': add,
        '-': sub,
        '*': multipy,
        '/': div
    }
    for token in tokens:
        if token not in opeartions_set:
            stack.append(int(token))
        else:
            if len(stack) > 1:
                stack.append((lambda b=stack.pop(), a=stack.pop(): operations[token](a, b))())
        print(stack)
    return stack[0]
            

# print(evalRPN( tokens = ["2","1","+","3","*"]))
# print(evalRPN( tokens = ["4","13","5","/","+"]))
print(evalRPN( tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
