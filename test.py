T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split)    
    matrix = [list(map(int, input().split())) for _ in range(N)] # 풍선정보

    # 상하좌우로 움직일 때 좌표의 변화량
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    # 최대값
    max_cnt = 0




    for r in range(N):

        for c in range(M): # 현재 위치 (r,c) # 현재 위치에 있는 풍선의 꽃가루 개수 = arr[r][c] # 여기에 상하좌우 풍선도 확인해서 꽃가루 개수 # 다 더해준 다음 최대값 구하기
            cnt = 0

            for d in range(4): # d는 방향

                nr = r + dr[d] # 다음 행,열 좌표

                nc = c + dc[d]

                if 0 <= nr < N and 0 <= nc < N: # 배열 내에 있을 때 !

                # 여기까지는 비슷(기본값)
            ###########################################################################################
                # 하고싶은 계산 ㄱㄱ    

                    cnt += matrix[nr][nc]


            max_cnt = cnt if cnt > max_cnt else max_cnt
            max_cnt =max(max_cnt, cnt)

    print(f'#{tc} {}')


