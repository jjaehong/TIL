# 정사각형 방
# bfs

def bfs(r, c, N):
    global rm
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    q = [(r, c)]

    cnt = 0
    while q:
        for _ in range(len(q)):
            r,c = q.pop(0)
            cnt += 1
            if v[r][c] != 0:
                return cnt + v[r][c] - 1

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < N and 0 <= nc < N and rm[r][c] + 1 == rm[nr][nc]:
                    q.append((nr, nc))
    return cnt


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    rm = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * N for i in range(N)]

    max_v = 0
    min_v = 1000000
    for r in range(N):
        for c in range(N):
            if v[r][c] == 0:
                v[r][c] = bfs(r, c, N)
                if (max_v < v[r][c]):
                    max_v = v[r][c]
                    min_v = rm[r][c]
                elif max_v == v[r][c]:
                    if min_v > rm[r][c]:
                        min_v = rm[r][c]

    print(f'#{tc} {min_v} {max_v}')
