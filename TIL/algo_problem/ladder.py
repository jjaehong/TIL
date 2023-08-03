for tc in range(1,11):
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    # 동남서북
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    for r in range(100):

        for c in range(100):
            if matrix[0][c] > 0:
                nr = 0
                nc = 0
                d = 0
                while r < 99:

                    if matrix[r][c-1] == 0 and matrix[r][c+1] ==0: # 오른쪽, 왼쪽이 0이면 계속 내려가라
                        d = 1
                    
                        if matrix[r][c-1] == 1: # 왼쪽 길에 1이면 왼쪽으로 간다.
                            d = 2

                        elif matrix[r][c+1] == 1: # 오른쪽 길에 1이면 왼쪽으로 간다.
                            d = 0
                            
            nr += dr[d]
            nc += dc[d]

        if matrix[nr][nc] == 2:
            result = nc
            break
    print(f'#{tc} {result}')