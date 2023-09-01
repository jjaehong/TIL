# 부분수열의 합
# 재귀 + 백트래킹

def f(i, N, s, K, rs):
    global cnt
    if i == N:
        if s == K:
            cnt += 1

    elif s > K: # 최적화
        return
    elif s + rs < K: # 최적화
        return

    else:
        f(i + 1, N, s + arr[i], K, rs-arr[i])
        f(i + 1, N, s, K,rs-arr[i])


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    f(0, N, 0, K)
    print(f'#{tc} {cnt}')
