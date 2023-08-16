# 괄호 검사(스택)
#
# 깨달은 점:
# 검사문제(True/False) = > 결과값 1이냐 0이냐
# 결과값 '1' 인경우 : 코드블록 안의 조건을 모두 False(0)로 해주면 됨. 안의 조건이 모두 해당이 안된다면 1로 나올테니!
# 결과값 '0' 인경우 : 코드블록 안의 조건을 모두 True(1)로 해주면 됨. 안의 조건이 모두 해당이 안된다면 0으로 나올테니!

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    row = input()  # 괄호의 짝이 맞는지 검사할 문자열

    stack = [] # 스택
    answer = 1 # 1이면 괄호가 제대로 되어있음, 0이면 괄호가 제대로 안되어있음.

    # 괄호 검사

    # row에서 한글자씩 떼어와서 검사
    for i in row:
        if i == '(' or i =='{':  # 떼어낸 한 글자가 만약 여는 괄호다? => 스택에 삽입
            stack.append(i)
        if i == ')' or i =='}':  # 떼어낸 글자가 닫는 괄호다 => 스택에서 하나 꺼내온 다음에
            if len(stack) == 0:  # 꺼내오기 전에 스택이 비어있나 확인, 비어있으면 오류!!
                answer = 0
                break

            p = stack.pop()
            if not ((p == '(' and i == ')') or (p == '{' and i =='}')): # 짝이 맞는지 검사 => 괄호의 종류가 다르면 오류!!
                answer = 0
                break

    if len(stack) != 0: # 모든 글자 검사가 끝난 후에 스택이 비어있지 않으면 오류
        answer = 0

    print(f'#{tc} {answer}')


