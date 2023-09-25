T = int(input())
for tc in range(1,T+1):
    N = int(input())
    P = list(input())
    key = int(input())

    H = [0]*N

    for i in range(N):
        H[i] = int(P[i],16) ^ key
    
    print(f'#{tc}', end = '')