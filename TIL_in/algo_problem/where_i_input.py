# 어디에 단어가 들어갈 수 있을까
# 1979


import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 0 # 단어가 들어갈 수 있는 자리의 수
    for r in range(N): # 행 우선 순회
        cnt = 0 # 연속한 빈칸(1)의 개수
        for c in range(N):
            if arr[r][c]: # arr[r][c]가 1이면
                cnt += 1
            if c == N-1 or arr[r][c]==0:
                if cnt == K:
                    answer += 1
                cnt = 0
    print(cnt)