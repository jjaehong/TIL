# 고대 유적

# N * M
# 행 순회, 열 순회 => '1'이 몇번이나 연속적으로 이어져있는가
# 고대 구조물 찾기
# 구조물 중 max값 찾기

import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 결과값
    max_len = 0


    # 고대 구조물 찾기



    # 행 우선순회 동쪽만 감

    for r in range(N):
        row_len = 0 #
        for c in range(M):
            if matrix[r][c] == 1:
                row_len += 1
                max_len = row_len if max_len < row_len else max_len
            else:
                row_len = 0

    # 열 우선순회 남쪽만 감
    for c in range(M):
        col_len = 0  #
        for r in range(N):
            if matrix[r][c] == 1:
                col_len += 1
                max_len = col_len if max_len < col_len else max_len
            else:
                col_len = 0

    print(f'#{tc} {max_len}')




    # # 윤형이 풀이 while + delta
    #
    # T = int(input())
    # # 우 아 왼 위
    # dr = [0, 1, 0, -1]
    # dc = [1, 0, -1, 0]
    # for tc in range(1, T + 1):
    #     N, M = map(int, input().split())
    #     site = [list(map(int, input().split())) for _ in range(N)]
    #
    #     max_len = 0
    #
    #     for r in range(N):
    #         for c in range(M):
    #             if site[r][c] == 1:
    #                 for d in range(4):
    #                     length = 1
    #                     nr = r + dr[d]
    #                     nc = c + dc[d]
    #                     while True:
    #                         if 0 <= nr < N and 0 <= nc < M and site[nr][nc] == 1:
    #                             length += 1
    #                             nr += dr[d]
    #                             nc += dc[d]
    #                         else:
    #                             break
    #                     if max_len <= length:
    #                         max_len = length
    #
    #     print(f'#{tc} {max_len}')

