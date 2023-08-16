icp = {'+' : 1, '*': 2}
isp = {'+' : 1, '*': 2}

# 중위표기식 -> 후위표기식
# 후위표기식 -> 계산



def get_postfix(infix,n):
    postfix = ''
    stack = []

    for i in range(n):

        if infix[i] not in '+*':
            postfix += infix[i]

        else:
            while stack and isp[stack[-1]] >= icp[infix[i]]:
                postfix += stack.pop()
            stack.append(infix[i])
    
    while stack:
        postfix += stack.pop()
    
    return postfix

def get_result(postfix):
    stack = []

    for c in postfix:
        if c not in '+*':
            stack.append(int(c))
        else:
            right = stack.pop()
            left = stack.pop()

            if c == '+':
                result = left + right
            elif c == '*':
                result = left * right

            stack.append(result)
    return stack[0]

            

import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1,11):
    n = int(input())
    row = input()
    postfix = get_postfix(row,n)

    print(f'#{tc} {get_result(postfix)}')

    