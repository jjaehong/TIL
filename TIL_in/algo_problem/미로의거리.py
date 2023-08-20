# 미로의 거리(그래프 탐색)

# 2차원 칸 그래프 탐색(출발지 -> 도착지) : dfs, bfs / 델타
# 최소 칸 수(경로) => bfs / visited에 경로 갯수 남기면서 
# 출발지 = 2, 도착지 = 3
# 도착점까지 경로 없으면 0 출력

# 그래프 탐색 문제
# 현재 위치 -> 다음 위치 탐색 (어떻게 탐색할건데?)
# visited : 중복 방문 방지 and 지나온 경로 갯수 세기
# 큐에 탐색할 곳 append(), 방문처리 / q에서 탐색 끝나면 pop(0)하고 다음 진행 => 이렇게 q를 채우고 비우면서 모든 곳 탐색

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
    visited = [[0] * n for _ in range(n)] # 2차원 방문기록(배열)
    q = []
    q.append((sr, sc)) # 튜플 유의 # 시작점 인큐하고 방문처리
    visited[sr][sc] = 1


    # q가 비면 모두 탐색, 그 때까지 계속 델타 탐색
    while q:

        # q를 단계별로 기록함(append(),pop(0))
        for _ in range(len(q)):
            r, c = q.pop(0)  # 현재 방문 위치 r,c
            if maze[r][c] == 3:  # 현재 방문하는 위치가 도착점인 경우 반복 중단
                return visited[r][c] - 2 # 0의 갯수를 세는 것이니 출발점, 도착점 제외하면 -2

            # 현재 위치 -> 다음 위치 탐색(델타)
            for d in range(4): # 현재 위치(r,c)에서 4방향 탐색
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

