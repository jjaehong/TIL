# 스도쿠 검증

# 스토리 : 행, 열, 3*3 검증 : 1~9 중복 X, 숫자가 겹치면 안됨


import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    matrix = [list(map(int, input().split())) for _ in range(9)]

    # 결과값
    answer = 1  # 스도쿠 완성되면 1, 아니면 0

    # 행 검증
    for r in range(9):
        cnt = [0] * 10  # 카운트 배열(1부터니까 10개 만듬)
        for c in range(9):
            cnt[matrix[r][c]] += 1
        for k in range(1, 10):
            if cnt[k] == 0:  # 1~9에 빠진 숫자가 있으면
                answer = 0
                break  # 함수 종료
        if answer == 0:
            break

    # 열 검증
    lst = []
    for c in range(9):
        cnt = [0] * 10  # 9+1 0을 안세기에
        for r in range(9):
            cnt[matrix[r][c]] += 1
        for k in range(1, 10):
            if cnt[k] == 0:  # 1~9에 빠진 숫자가 있으면
                answer = 0
                break  # 함수 종료
        if answer == 0:
            break

    # 3*3 검증
    for r in range(0, 7, 3):
        for c in range(0, 7, 3):
            cnt = [0] * 10
            for i in range(3):
                for j in range(3):
                    cnt[matrix[i][j]] += 1
                for k in range(1, 10):
                    if cnt[k] == 0:
                        answer = 0
                        break
                    print(matrix[i][j])
    print(f'#{tc} {answer}')

    # 3*3 검증
