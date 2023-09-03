n = 7
arr = [[0]* n for _ in range(n)]

# ===============================
# 8방향 탐색
dr = [-1,-1,-1,0,1,1,1,0]
dc = [-1,0,1,1,1,0,-1,-1,]

r=c=2
arr[r][c] = '*'
for i in range(8): # 방향 결정
    for j in range(1,n): # 거리
        nr = r + dr[i]*j
        nc = c + dc[i]*j
        if 0<= nr < n and 0<=nc < n:
            arr[nr][nc] = i + 1


# ===============================

for line in arr:
    print(*line)



