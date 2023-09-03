
# 죽은 파리 최대 

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]


    
    dead_max = 0
    # 파리채 몇번 활용가능?
    for i in range(N-M+1):
        for j in range(N-M+1):
            
            dead_sum = 0
            # 파리채 만들기
            for r in range(i,i+M):
                for c in range(j,j+M):
                    dead_sum += matrix[r][c]
            
            dead_max = max(dead_max,dead_sum)

    print(f'#{tc} {dead_max}')
                



    