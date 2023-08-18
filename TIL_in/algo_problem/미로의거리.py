# 미로의 거리

# 동남서북
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 출발지점 설정
def start_point():
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                return i, j

def bfs(sr, sc):

    # 기본설정
    visited = [[0] * n for _ in range(n)]
    q = []
    q.append((sr, sc))
    visited[sr][sc] = 1


    # 계속 델타 탐색
    while q:
        # 계층마다 한번에 q를 pop()하겠다
        for _ in range(len(q)):
            r, c = q.pop(0)  # 현재 방문하는 위치 r,c
            if maze[r][c] == 3:  # 현재 방문하는 위치가 도착점인 경우 반복 중단
                return visited[r][c] - 2 # 0의 갯수를 세는 것이니 출발점, 도착점 제외하면 -2

            # 현재 위치 r,c에서 4방향 탐색
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                # 다음 위치가 유효한 인덱스인지, 벽이아님, 방문한적도 없음
                if 0 <= nr < n and 0 <= nc < n and maze[nr][nc] != 1 and visited[nr][nc] == 0:
                    # 새로운 위치 인큐 + 방문기록도 남기자 근데 지금까지 몇개 거쳐서 왔는지도 남기자
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1 #

    return 0 # 방문못하면 0


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]

    sr,sc = start_point()

    print(f'#{tc} {bfs(sr,sc)}')

