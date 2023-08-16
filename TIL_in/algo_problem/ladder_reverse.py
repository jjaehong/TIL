import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    int(input())  # 테스트 케이스 번호 입력 처리
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 내가 위치를 직접 움직여야 한다.
    # 아래에서부터 거꾸로 올라가기

    # 아래 출발점 찾기 = 2

    r = 99
    c = -1 # 값을 찾을 때 임시저장 : -1

    for i in range(100):
        if ladder[r][i] == 2:
            c = i

    # 좌, 우, 상
    dr = [0,0,-1]
    dc = [-1,1,0]

    # 왼쪽이나 오른쪽에 길이 있으면 그냥 가버림
    # 왼쪽이나 오른쪽에 길이 없으면 위로 간다.

    while r > 0:
        for d in range(3): # 방향지정 # 이동할 때마다 좌 => 우 => 상으로 봄
            nr = r + dr[d] # 새로운 좌표 찍기
            nc = c + dc[d]

            if 0<= nr < 100 and 0<= nc < 100 and ladder[nr][nc] == 1:
                r = nr   # 갈수 있으면 간다.
                c = nc   # 현재 위치를 최신화
                ladder[r][c] = 0
                break # 반복문이 끝나면 r이 0이 되었을 거니까 출력

    print(f'#{tc} {c} ')