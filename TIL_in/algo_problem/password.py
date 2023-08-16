# 비밀번호

# 스토리

# 깨달은 점

import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, T+1):
    str_n, str_num = input().split()

    # 스택 기본설정
    n = int(str_n)
    stack = [0] * n
    top = -1

    # 인덱스 접근? or 하나씩 가져와?
    for t in str_num:
        if top == -1 or stack[top] != t: # 스택이 비어있거나, top 원소와 다르면
            top += 1 # push(t)
            stack[top] = t
        else:                            # 스택이 비어있지 않고 top과 같으면
            top -= 1

    # 출력 방법 1
    ans = ''
    for i in range(top+1):
        ans += stack[i]
    print(f'#{tc} {ans}')

    # 출력 방법 2
    # ans = ''.join(stack[:top+1])
    # print(f'#{tc} {ans}')