# 풍선팡2
# 16268

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N,M  = map(int,input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    max_v = 0 # 초기화
    for r in range(N):
        for c in range(M):
            cnt = matrix[r][c] # [r][c]중심 + [nr][nc]edge 초기화 # matrix[r][c] 값만 저장  
            for d in range(4):
                nr, nc = r+dr[d], c + dc[d]
                if 0 <= nr < N and 0<= nc < M:
                    cnt += matrix[nr][nc] # 중심과 edge 풍선까지 더한 값
            if max_v < cnt: # 그 값 중 max값 
                max_v = cnt
    
    print(f'#{tc} {max_v}')
                


            

