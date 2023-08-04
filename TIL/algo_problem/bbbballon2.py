# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N,M  = map(int,input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    max_v = 0 # 초기화
    for r in range(N):
        for c in range(M):
            cnt = matrix[r][c] # rc중심으로 터트린 풍선의 꽃가루 수 # 
            for d in range(4):
                nr, nc = r+dr[d], c + dc[d]
                if 0 <= nr < N and 0<= nc < M:
                    cnt += matrix[nr][nc]
            if max_v < cnt: # r,c 인접 풍선까지 더하고나면
                max_v = cnt
    
    print(f'#{tc} {max_v}')
                


