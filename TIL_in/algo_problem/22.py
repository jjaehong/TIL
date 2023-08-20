# 미로거리 bfs
# 현재 위치 -> 다음 위치(델타)

dr = [0,1,0,-1]
dc = [1,0,-1,0]


def start():
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                return r, c
    
def bfs(sr,sc):

    # 기본설정
    visited = [[0] * N for _ in range(N)]
    q = []
    q.append((sr,sc))
    visited[sr][sc] = 1

    # q가 빌때까지 방문, 모두 방문
    while q:

        for _ in range(len(q)):
            r,c = q.pop(0) # 현재 위치 지정
            if maze[r][c] == 3:
                return visited[r][c]
            
            for i in range(N):
                for j in range(N):
                    if (i, j) == (r, c):
                        print("*", end=" ")
                    else:
                        print(maze[i][j], end=" ")
                print()
            print("===================")

            for d in range(4):
                for d2 in range(1, visited[r][c] + 1,2):
                    nr = r + dr[d] * d2
                    nc = c + dc[d] * d2
                    if 0<= nr < N and 0<= nc < N and maze[nr][nc] != 1 and visited[nr][nc] ==0:
                        q.append((nr,nc))
                        visited[nr][nc] = visited[r][c] + 1
    return 0






import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    sr,sc = start()

    print(f'#{tc} {bfs(sr,sc)}')