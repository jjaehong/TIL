

for tc in range(1,11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 교착 수
    cnt = 0

    for j in range(N):
        tmp = 0
        for i in range(N):
            if arr[i][j] == 2 and tmp ==1:
                cnt += 1
                tmp = 0
            elif arr[i][j] == 1:
                tmp = 1
    print(f'#{tc} {cnt}')