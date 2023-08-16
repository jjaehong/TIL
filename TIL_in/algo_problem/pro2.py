# 괄호연산

# 정수, (), {}

# 가장 안쪽 괄호 먼저 계산
# 소괄호 : 더하기
# 중괄호 : 곱
# 괄호 짝 안맞으면 -1 출력

# 1. 수식 괄호 검사(짝 검사)
# 2. 식 계산
# 3. 나머지 -1
T = int(input())
for tc in range(1, T + 1):
    row = input()

    stack = []
    answer = 0


    if not ((row[0] == '(' and row[-1] == ')') or (row[0] == '{' and row[-1] == '}')): # 괄호안에 숫자가 없으면 -1
        answer = -1

    for i in row:

        if i.isalpha(): # 문자열이면 -1
            answer = -1

        if i == '(' or i == '{':
            stack.append(i)

        if i == ')' or i == '}':  # 스택에 남은 것이 없다면 짝 안맞음
            if len(stack) == 0:
                answer = -1
                break

            p = stack.pop()
            if not ((p == '(' and i == ')') or (p == '{' and i == '}')):  # 짝 검사
                answer = -1
                break

    if len(stack) != 0:
        answer = -1

    print(f'#{tc} {answer}')
