# 우주선 착륙2

# 중심부에서 주변부 검사 ( 중심부가 더 크면 cnt+1, cnt>=4
# cnt >= 4 면 예비후보지 채택

import sys

sys.stdin = open("input.txt", 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    #    동 동남 남 남서 서 서북 북 북동
    dr = [0, 1, 1, 1, 0, -1, -1, -1]
    dc = [1, 1, 0, -1, -1, -1, 0, 1]

    result = 0

    for r in range(N):
        for c in range(M):
            cnt = 0
            for d in range(8):  # 8방향 검사
                nr = r + dr[d]
                nc = c + dc[d]

                if 0 <= nr < N and 0 <= nc < M and matrix[r][c] > matrix[nr][nc]:
                    cnt += 1

            if cnt >= 4:
                result += 1

    print(f'#{tc} {result}')
