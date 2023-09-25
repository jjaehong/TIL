<<<<<<< HEAD
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    P = list(input())
    key = int(input())

    H = [0]*N

    for i in range(N):
        H[i] = int(P[i],16) ^ key
    
    print(f'#{tc}', end = '')
=======
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
>>>>>>> 0c88bf1ace56454836add055d30d0c6bad734f9a
