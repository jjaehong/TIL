T = int(input())
for tc in range(1, T+1):
    # 바운스 챌린지 횟수
    N = int(input())

    arr = list(map(int, input().split()))

    result = 0

    # 챌린지는 N번 시도
    # n번 시도할때마다 합을 구하는 방식이 다르다.
    # 1칸씩 증가, 2칸씩 증가 ... N칸씩 증가

    for i in range(N):
        # i번째 챌린지의 합을 구하는 방식
        # i+1만큼 움직이면서 합을 구한다.

        for j in range(0,N,i+1):
            result += arr[j]

    result = result if result >= 0 else 0


    print(f'#{tc} {result}')


