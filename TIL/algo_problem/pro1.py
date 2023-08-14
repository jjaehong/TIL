# 봉우리
# 어떤 지역의 높이 > 모든 인접지역(상하좌우 4곳) 높이 : 봉우리
# 봉우리 해당하는 모든지역 찾기

# 행 순회하며 중심점 하나씩 검사
# 인접지역보다 높은지?
# 산봉우리 조건이 2인 경우, 3인 경우, 4인 경우 나눠서 결과값에 더하기

# 혹시 조건이 복잡해진다면 조건 반대의 경우를 생각해보자!
# 주변부가 더 높다면? break
# 나머지를 cnt + 1, cnt 출력


import sys
sys.stdin = open('pro1.txt', 'r')

# 주변부를 count 함.
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 동남서북
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # 산봉우리 개수
    san = 0

    for r in range(N):
        i = r
        for c in range(N):
            j = c
            cnt = 0
            for d in range(4):  # 4방향 지정
                nr = r + dr[d]
                nc = c + dc[d]

                if 0 <= nr < N and 0 <= nc < N and matrix[r][c] > matrix[nr][nc]:
                    cnt += 1

            if (((r, c) == (0, 0)) or ((r, c) == (0, (N - 1))) or ((r, c) == ((N - 1), 0)) or ((r, c) == ((N - 1), (N - 1)))) and cnt == 2:
                san += 1

            elif ((r, c == i, 0) or (r, c == 0, j) or (r, c == i, (N - 1)) or (r, c == (N - 1), j)) and cnt == 3:
                san += 1

            else:
                if cnt == 4:
                    san += 1

    print(f'#{tc} {san}')

# # 반대의 경우를 생각
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     matrix = [list(map(int, input().split())) for _ in range(N)]
#
#     # 동남서북
#     dr = [0, 1, 0, -1]
#     dc = [1, 0, -1, 0]
#
#     # 산봉우리 개수
#     cnt = 0
#     for r in range(N):
#         for c in range(N):
#             for d in range(4):  # 4방향 지정
#                 nr = r + dr[d]
#                 nc = c + dc[d]
#
#                 if 0 <= nr < N and 0 <= nc < N and matrix[r][c] <= matrix[nr][nc]: # 중심부보다 주변부가 하나라도 더 높으면 안돼
#                     break
#             else: # 주변부 전체 보다 중심부가 더 높은 경우
#                 cnt += 1
#
#     print(f'#{tc} {cnt}')
