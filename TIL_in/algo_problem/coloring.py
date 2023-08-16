import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    n = int(input())

    paper = [[0] * 10 for _ in range(10)] # 종이 10*10
    
    purple_count = 0 # 보라색 칸 개수(겹친 개수)

    # n번 반복하면서 색칠하는데 겹친 칸 개수 세기
    for i in range(n):
        sr, sc, er, ec, color = map(int, input().split())

        # 색칠 범위

        # 색칠 시작 행~ 색칠 끝 행
        for r in range(sr,er+1):
        # 색칠 시작 열 ~ 색칠 끝 열
            for c in range(sc,ec+1):
                # 색칠 하기 전에 봐야 할 것
                # 다른 색이 있다면 보라색이 된다.
                if paper[r][c] == 0:
                    paper[r][c] = color
                else:
                    # 0이 아니면 다른색이 칠해져 있었다. => 보라색
                    purple_count += 1
    
    print(f'#{tc} {purple_count}')


# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())

#     # 도화지 만들기
#     matrix = [[0] * 10 for _ in range(10)]
#     purple_area = 0

#     for i in range(N):
#         sr, sc, er, ec, color = map(int, input().split())

#         # 네모 형태 만들기
#         for r in range(sr, er + 1):
#             for c in range(sc, ec + 1):
#                 # 빨강, 파랑 색칠하기
#                 if color == 1:
#                     matrix[r][c] += 1
#                 elif color == 2:
#                     matrix[r][c] += 2

#                 if matrix[r][c] == 3:
#                     purple_area += 1


#     print(f'#{tc} {purple_area}')
#     print(matrix)