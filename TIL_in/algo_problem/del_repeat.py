# 반복문자 지우기

# 리스트와 for문으로 풀기
# 문자열을 리스트로 받음
# 리스트 안에 인덱스로 연속된 문자열이 같으면 둘 다 지워줌.(i,i+1)
# 지우는 것을 for문으로 n번 반복해줌.

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    s = input()

    lst = []
    lst.extend(s)
    # while lst != s:
    for _ in range(len(s) // 2):  # len(s)//2만큼 반복해줘 !

        for i in range(0, len(lst) - 1):
            if lst[i] == lst[i + 1]:
                lst.pop(i + 1)
                lst.pop(i)
                break  # break는 break를 받는 반복문을 종료
                # 그럼 위의 for문 다시 반복 시작

    print(f'#{tc} {len(lst)}')


    # 스택으로 풀기
    size = 1000
    stack = [0] * size
    top = -1
    # 일단 문자를 스택에 넣어(맨 처음 글자는 넣음)
    top += 1
    stack[top] = s[0]

    # 두번째 글자부터는 내가 제일 최근에 넣었던 글자와 비교해서
    for i in range(1, len(s)):
        # 만약 같다면 스택에서 pop
        if top != -1 and stack[top] == s[i]:
            top -= 1
        # 다르다면 현재 글자를 스택에 push
        else:
            top += 1
            stack[top] = s[i]

    print(f'#{tc} {top + 1}')  # 인덱스를 활용한 스택은 지워도 그 안에 데이터는 남아있는 상태이니 인덱스 + 1 해줘야 길이가 나온다.



