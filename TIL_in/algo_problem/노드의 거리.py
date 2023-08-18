# 노드의 거리(인접리스트 접근)

# q에서 탐색할 곳은 append() / q에서 탐색 끝나면 pop()
# 현재 방문 -> 다음 방문

# 최소 거리 탐색 => 너비 우선 탐색 
def bfs(s,V):

    # 기본설정
    visited = [0] * (V+1) # 방문배열 만들고(중복방문방지)
    q = [] # 큐 배열 만들고
    q.append(s) # 시작점 인큐
    visited[s] = 1 # 시작점 방문

    # q가 비면 모두 탐색한 거임
    while q:

        # 종료 조건
        if visited[G] != 0: # 도착지 방문했으면
            # print(f'now : {now}', end=" ")
            return visited[G] - 1 # 도착지까지 최소 간선 개수 반환

        # 같은 계층 단계를 기준으로 묶어서 pop하고 append함 => q가 단계별로 기록됨
        for _ in range(len(q)):
            now = q.pop(0) # 현재 방문 위치. q에서 꺼내기

            # 현재 위치에서 갈 수 있는 곳 찾기
            for next in adj_l[now]: # 현재 위치(now)에서 연결된 모든 다음 정점(next)를 탐색
                if visited[next] == 0: # 다음 정점을 방문한 적이 없다면
                    q.append(next) # q에 탐색할 곳으로 추가
                    visited[next] = visited[now] + 1 # 방문기록 남기고 거기까지 가는데 든 거친 노드수 추가
                    # print()
                    # print(f'q : {q}')
                    # print(f'visited : {visited}')

    # 다 돌았는데도 도착점을 못찾으면
    return 0

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())  # v: 노드 수, e : 간선 수
    adj_l = [[] for _ in range(V+1)]

    for _ in range(E):
        s, e = map(int, input().split())
        adj_l[s].append(e)
        adj_l[e].append(s)
    # print(adj_l)
    S,G = map(int, input().split()) # 시작점, 도착점

    print(f'#{tc} {bfs(S,V)}')
