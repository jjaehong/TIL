# 현주 상자
# 인덱싱 연습

import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1,T+1):
    N,Q = map(int, input().split())
    
    C = [0]*(N)
    for i in range(1,Q+1): # 작업 Q번 시도
        L, R= map(int, input().split())
        for j in range(L-1,R+1): # L~R까지 i로 바꿔라 
            C[j] = i

    print(f'#{tc}',*C)





        
        