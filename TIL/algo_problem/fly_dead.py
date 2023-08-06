T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0

    # 파리채 몇 번 활용가능?
    for i in range(N-M+1):
        for j in range(N-M+1):
            dead_sum = 0

            # 파리채 만들기
            for r in range(i,i+M): # 파리채 별로 r시작위치 ~ r끝위치 
                for c in range(j,j+M):
                    dead_sum += matrix[r][c]

            max_v = dead_sum if max_v < dead_sum else max_v

    print( f'#{tc} {max_v}')