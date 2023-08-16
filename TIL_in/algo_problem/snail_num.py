T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 동남북서
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    # 달팽이 집을 0으로 다 채워서 N*N 만큼 만들어주기
    snail = [[0]* N for _ in range(N)]

    # 달팽이집 채우기 (0,0) 고정
    # N * M 번 반복하면서 채워간다
    # 방향은 동 => 남 => 서 => 북

    d = 0 # d는 현재 채워나가는 방향
    r,c = 0,0 # 시작 위치

    for i in range(1, (N*N) + 1):
        snail[r][c] = i

        # 다음 방향으로 진행
        # 다음 위치가 유효한 위치인지

        nr = r + dr[d]
        nc = c + dc[d]

        # 다음 위치가 유효하지 않으면 방향 꺾기
        # nr, nc가 인덱스 범위 밖으로 벗어나면 꺾고
        # 다음 위치가 0이 아니어도 꺾고

        if 0<= nr < N and 0 <= nc < N and snail[nr][nc] == 0: # 순서 바뀌면 안됨!!!!
            # 다음 위치가 유효하면 계속 가고
            r, c = nr, nc
        else:
            # 유효하지 않으면 방향 꺾기

            # d = d+1 if d < 3 else 0

            # if d< 3:
            #     d=d+1
            # else:
            #     d = 0
            d = (d+1) % 4
            r = r+ dr[d]
            c = c+ dc[c]

    # print(*snail, sep="\n")
    print(f'#{tc}')
    for i in range(N):
        print(" ".join(map(str,snail[i])))





