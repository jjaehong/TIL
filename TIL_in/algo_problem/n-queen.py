# n-queen

# row : 현재 행 번호
# remain : 놓아야 할 퀸의 남은 개수

def backtracking(row, remain):

    global cnt

    # 1. 종료 조건
    if row == N and remain==0:
        cnt += 1
        return 


    # 2. 재귀 호출
    # 현재 row행에서 i번째 열에 퀸을 놓을 수 있으면 놓고 row+1 행에 퀸 놓으러 가기
    for i in range(N):
        # i번째 열에서 퀸을 놓을 수 있는가?
        can_place = True

        # 세로에 퀸이 있는지 검사(row까지 검사.. 왜? : )
        for j in range(row):
            if board[j][i] == 1:
                can_place = False
                break

        # 대각선에 퀸이 있는지 검사(좌상,우상 대각선만 검사해도됨.. 왜? : 아래는 내려오면서 자동검사되니까)
        for j in range(row):
            # 좌상
            if row - j >= 0 and i-j >=0 and board[row-j][i-j] == 1:
                can_place = False
                break
            # 우상
            if row-j >=0 and i + j < N and board[row-j][i+j] == 1:
                can_place = False
                break
        
        # 세로와 대각선 검사를 다 했는데, i번째 열에 퀸을 놓을 수 있대!!
        if can_place:
            # 놓을 수 있으면 현재 위치에 놓고 다음 위치로 이동 ==> 재귀 호출
            board[row][i] = 1
            # row +1에 퀸 놓으러가기, 남은 퀸 개수 -1
            backtracking(row+1,remain-1)
            # 다시 되돌려놓고 진행
            board[row][i] = 0



T = int(input())
for tc in range(1,T+1):
    N = int(input())

    # 경우의 수
    cnt = 0

    # 보드 만들기
    board = [[0]* N for _ in range(N)]
    backtracking(0,N)

    print(f'#{tc} {cnt}')