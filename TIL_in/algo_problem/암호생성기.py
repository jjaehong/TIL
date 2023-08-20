# 암호생성기
# password q삽입
# 뒤로 보내기(앞 삭제, 삭제한 것을 rear에 삽입)

import sys
sys.stdin = open('input.txt', 'r')


for tc in range(1,11):
    int(input())
    password = list(map(int, input().split()))

    # 초기화
    q = [0] * 100000
    front = rear = -1

    # q에 패스워드 삽입
    for i in range(8):
        rear += 1
        q[rear] = password[i]
    

    answer = ''
    # 맨 뒤의 값이 0이 될때까지 뒤로 보내기
    while True:
    
        # 한 사이클 돌기 
        for j in range(1,6): 
            front += 1
            d = q[front]
            rear += 1
            q[rear] = d - j # 뒤로 보내면서 1~5만큼 빼주기

            # while 탈출
            if q[rear] <= 0:
                q[rear] = 0
                break

        if q[rear] == 0:
            for k in range(front+1, rear+1):
                answer += str(q[k])
            break

    print(f'#{tc}', *answer)
