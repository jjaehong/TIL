'''
6528-*2/+
'''

stack = [0] * 100
top = -1
susik = '6528-*2/+'
for x in susik:
    if x not in '+-/*':# 피연산자면..
        top += 1 # push(x)
        stack[top] = int(x)
    else:
        op2 = stack[top]  # pop()
        top -= 1
        op1 = stack[top]  # pop()
        top -= 1

        if x == '+': # op2 + op1
            top += 1
            stack[top] = op1 + op2

        elif x == '-':
            top += 1
            stack[top] = op1 - op2

        elif x == '/':
            top += 1
            stack[top] = op1 / op2

        elif x == '*':
            top += 1
            stack[top] = op1 * op2
print(stack[top])
