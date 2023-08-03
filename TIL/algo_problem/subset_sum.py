import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())  # 원소의 개수 # 원소의 합

    A = list(range(1, 13))

    cnt = 0
    for i in range(1 << 12):

        a = 0
        b = 0
        for j in range(12):
            if i & (1 << j):
                a += 1
                b += A[j]

        if a == N and b == K:
            cnt += 1


    print(f'#{tc} {cnt}')