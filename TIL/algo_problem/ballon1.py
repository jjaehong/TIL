# 풍선팡

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N,M  = map(int,input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 동남서북
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    max_v = 0 
    for r in range(N):
        for c in range(M):
            cnt = matrix[r][c] # rc중심으로 터트린 풍선의 꽃가루 수 저장
            for d1 in range(4): # 움직이는 방향 지정
                for d2 in range(1, matrix[r][c]+ 1): # cnt만큼 더 터트림

                # 만약 그냥 중심점 기준으로 n개 터트리고 싶다! for d2 in range(1,n+1)

                    nr, nc = r + dr[d1]*d2, c + dc[d1]*d2 # 1 ~ d2칸만큼 다 채워가며 더 갈거야
                    if 0<= nr < N and 0 <= nc < M:
                        cnt += matrix[nr][nc] # 주변칸 풍선의 꽃가루 수
            if max_v < cnt:
                max_v = cnt
    print(f'#{tc} {max_v}')


