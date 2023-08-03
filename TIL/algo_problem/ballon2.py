import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):

    N,M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    
    max_vs = 0
    for r in range(N):
        for c in range(M): # matrix 생성
            
            edge = 0 

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0<= nr < N and 0 <= nc < N:        
                    edge += matrix[nr][nc]

            max_vs = edge + matrix[r][c] if max_vs < edge + matrix[r][c] else max_vs 
            


    print(f'#{tc} {max_vs}')

                


            

