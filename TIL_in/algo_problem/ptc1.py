

import sys
sys.stdin = open('input.txt','r')

# 현재 i번째 행에서 j번째 열을 골라서 합을 만들기

def backtracking(r,now_sum):
    global min_v

    if now_sum > min_v:
        return

    # 종료조건
    if r == N:
        min_v = min(min_v,now_sum)
        return

    # 재귀 들어가기전

    # 재귀호출
    for c in range(N):
        # 선택안했다면
        if selected[c] == 0 :
            selected[c] = 1
            backtracking(r+1, now_sum + matrix[r][c])
            selected[c] = 0
    # 재귀 들어간 후


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]

    selected = [0] * N

    min_v = 10* N

    backtracking(0,0)

    print(f'#{tc} {min_v}')

