# 인접리스트

def dfs1(s,V):
    
    visited = [0] * (V+1)
    stack = []

    visited[s] = 1
    print(s)
    i = s

    while True:
        # 현재 정점 i에서 갈 수 있는 정점 j 찾기
        for j in adj_l[i]:
            # j는 i와 연결되어 있는 정점임
            # j를 방문한 적이 있는지만 확인하고 탐색
            if visited[j] == 0:

                stack.append(i) # 전 정점 스택에 저장
                visited[j] = 1 # 방문
                print(j) # 방문 후 할 일
                i = j # 새로운 i에서 탐색시작
                break
        else:
            if len(stack):
                i = stack.pop()
            else:
                break
    return




# V는 정점의 개수 E는 연결된 줄의 수
V, E = map(int,input().split())

# 인접 리스트
adj_l = [[] for _ in range(V + 1)] #위의 문제에서는 0번 인덱스가 필요없기 때문에
for _ in range(E):
    # 연결이 되려면 연결 시작점 s, 연결 종료점 e
    s, e = map(int, input().split())
    # 만약 인접 행렬이라면
    # adj_m[s][e] = 1
    # adj_m[e][s] = 1
    adj_l[s].append(e)
    adj_l[e].append(s)

dfs1(1,V)