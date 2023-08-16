# 농작물 수확하기

# 스토리

# 깨달은 점: 다른 문제에서도 중심점과 끝 점과의 거리 차이로 문제 많이 풀 수 있음

T = int(input())
for tc in range(1, T +1):
    N = int(input())


    # 농작물 정보
    field = [list(map(int, input())) for _ in range(N)]

    # 수확한 농작물
    crops = 0

    # 밭의 정중앙과의 거리가 d이하인 곳만 수확
    d = N//2

    # 밭의 중앙 좌표
    center = (d,d)

    for r in range(N):
        for c in range(N):
            # 거리계산 방법
            # abs|r-d| + abs|c-d| <= 3이면 농작물 수확
            if abs(r-d) + abs(c-d) <= d:
                crops += field[r][c]

    print(f'#{tc} {crops}')

    # 인덱스로도 풀 수 있음

    # 한칸씩 늘어남, 한칸씩 줄어듬
    # r //2 > n 부터는
    # 한칸씩 줄어듬, 한칸씩 늘어남
