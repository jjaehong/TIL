from heapq import heappop, heappush
 
INF = 100000000
 
def dijkstra(s):
    q = []
    heappush(q, (0, s))
    D[s] = 0
 
 
    while q:
        w, v = heappop(q)
 
        if D[v] < w:
            continue
 
        for u, uw in adj_l[v]:
            cost = D[v] + uw
            if cost < D[u]:
                D[u] = cost
                heappush(q, (cost, u))
 
 
T = int(input())
 
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(0, E)]
    adj_l = [[] for _ in range(N+1)]
    for i in graph:
        s, e, w = i[0], i[1], i[2]
        adj_l[s].append((e, w))
 
    D = [INF] * (N+1)
 
    dijkstra(0)
     
    print(f"#{tc} {D[N]}")
