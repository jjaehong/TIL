# 미로1

# 2차원 그래프 탐색 => dfs, bfs
# 도착지점 갈 수 있는 길이 있는지 판단(1 or 0)

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def start():
    for r in range(16):
        for c in range(16):
            if maze[r][c] == 2:
                return r,c

def bfs(sr,sc):

    # 기본설정
    visited = [[0] * 16 for _ in range(16)]
    q = []
    q.append((sr,sc))
    visited[sr][sc] = 1

    # 모두 탐색할 때까지 == q가 빌때까지
    while q:

        for _ in range(len(q)):
            r,c = q.pop(0) # 현재 위치 r,c

            if maze[r][c] == 3:
                return 1
        
            for d in range(4): # 현재 위치에서 4방향 탐색
                nr = r + dr[d]
                nc = c + dc[d]
                # 갈 수 있고, 방문한 적 없으면 => 새로운 지점 인큐, 방문처리 => pop(0)하면 현재 위치(r,c) 초기화
                if 0<= nr < 16 and 0<= nc < 16 and maze[nr][nc] != 1 and visited[nr][nc] ==0:
                    q.append((nr,nc))
                    visited[nr][nc] = 1

    return 0


import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1,11):
    int(input())
    maze = [list(map(int, input())) for _ in range(16)]


    sr, sc = start()
    print(f'#{tc} {bfs(sr,sc)}')

