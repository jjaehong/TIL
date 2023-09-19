# n-queen


def backtracking():



T = int(input())
for tc in range(1,T+1):
    N = int(input())

    # 경우의 수
    cnt = 0

    # 보드판
    board = [[0]*N for _ in range(N)]
    
