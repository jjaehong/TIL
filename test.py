icp = {"+": 1, "-": 1, "/": 2, "*": 2, "(": 3}
isp = {"+": 1, "-": 1, "/": 2, "*": 2, "(": 0}


def get_postfix(infix,n):
    postfix = ''
    stack = []

    for i in range(n):
        
        if infix[i] not in '+':
            postfix += infix[i]
        
        else:
            # 닫는괄호라면
            if infix[i] == ')':

                while stack:
                    temp = stack.pop()
                    if temp =='(':
                        break
                    postfix += temp
            # 다른 연산자라면
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
        if c not in '+':
            stack.append(int(c))
        else:
            right = stack.pop()
            left = stack.pop()

            if c == '+':
                result = left + right
            
            stack.append(result)
    
    return stack[0]


import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1,11):
    n = int(input())
    row = input()
    postfix = get_postfix(row,n)

    print(f'#{tc} {get_result(postfix)}')