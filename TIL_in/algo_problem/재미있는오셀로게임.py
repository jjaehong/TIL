def f(i,j,bw,N):
    board[i][j] = bw




b=1
w=2


T = int(input())
for tc in range(1,T+1):
    N,M= map(int,input().split()) # N : 보드 크기 / M : 돌을 놓는 횟수
    x,y,color = [list(map(int,input().split())) for_ in]

    board = [[0]*N for _ in range(N)]       # 0 -> N-1까지
    
    
    # 중심부 4개의 돌 배치,

    board[N//2-1][N//2-1] = w

