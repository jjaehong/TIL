# 연산
# 사용 연산 4가지... 상하좌우 델타와 유사
# 최소 ~번 연산 -> BFS


# bfs 비슷 예시
# 디저트 카페
# 등산로 조성
from collections import deque

def bfs(n):

    # 기본설정
    # stack = deque()
    q = deque()
    visited = [0] * (1000000+1) # 중복 방문 x, 가짓수 줄여주기 위해 방문배열 생성
    q.append(n)
    visited[n] = 1

    # 연산횟수
    cnt = 0

    while q:
        
        # len(q)만큼 반복하면 한 단계 끝
        for _ in range(len(q)):
            now = q.popleft()

            if now == M:
                return cnt
            
            for next in [now+1,now-1,now*2,now-10]:
                if 1<= next <= 1000000 and visited[next] == 0:
                    q.append(next)
                    visited[next] = 1
        cnt += 1


T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split()) # N -> M

    print(f'#{tc} {bfs(N)}')
