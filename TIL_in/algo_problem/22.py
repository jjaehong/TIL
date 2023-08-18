# BFS / 미로찾기
# 인접행렬로 접근

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# sr : 시작 행 번호
# sc : 시작 열 번호
def bfs(sr, sc):
    # 중복 체크 배열
    visited = [[0] * n for _ in range(n)] # 인접행렬
    q = []
    q.append((sr, sc))  # 시작 위치 정보 (sr,sc)를 큐에 삽입
    visited[sr][sc] = 1

    # 탈출하는데 걸린 거리(최소)
    distance = 0
    while q:
        # 원소를 꺼내기 전에 현재 단계에서 큐안에 방문할 원소의 개수를 확인
        # 현재 단계에서 큐의 원소를 몇개까지만 확인하면 될지 직접 계산
        
        # 즉, bfs 같은 계층 단계를 기준으로 pop하고 append함
        size = len(q)
        for _ in range(size):
            r, c = q.pop(0)  # 현재 방문하는 위치 r,c

            # 현재 방문하는 위치가 도착점인 경우 반복 중단
            if maze[r][c] == 99:
                print(f"탈출 : {distance}")
                break

            # 현재 위치 r,c에서 4방향 탐색
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                # 다음 위치가 유효한 인덱스인지, 벽이아님, 방문한적도 없음
                if 0 <= nr < n and 0 <= nc < n and maze[nr][nc] != 1 and not visited[nr][nc]:
                    # nr, nc 방문 처리
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1

        distance += 1

    return distance


n = 7

maze = [[0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 99, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 1]]

maze = [[0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]

print(bfs(3, 3)) # (3,3)에서 시작
