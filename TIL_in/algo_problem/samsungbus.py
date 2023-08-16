# 삼성시의 버스 노선

import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cnt = [0] * 5001 # 1-5000번 각 정류장을 지나는 노선 수
    for _ in range(N): # N개의 노선에 대해
        A, B = map(int, input().split())
        for i in range(A,B+1):
            cnt[i] += 1 # 현재 노선이 i번 정류장 도착
    # print(cnt)


P = int(input())
bus_stop = [int(input()) for _ in range(P)]
# print(bus_stop)
print(f'#{tc}', end = ' ')
for x in bus_stop:
    print(cnt[x], end = ' ')
print()

