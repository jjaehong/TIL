# 전기버스
# 사고력이 중요..

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split()) # k 한번충전 최대이동거리 # n은 종점 정류장(0~n) # m 충전기가 설치된 m개의 정류장 
    charge = list(map(int,input().split())) # 충전기가 설치된 정류장 번호들
 
    bus = 0  # 버스 현재 위치
    count = 0 # 충전 횟수
 
    while bus + K < N:
        for i in range(K,0,-1):
            if (bus + i) in charge:
                bus = bus + i
                count += 1
                break
        else:
            count = 0
            break
         
    print(f'#{tc} {count}')