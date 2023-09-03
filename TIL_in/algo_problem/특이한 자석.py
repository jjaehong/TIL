# 특이한 자석

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    K = int(input())    # 자석 회전시키는 횟수
    matrix = [list(map(int, input().split())) for _ in range(4)] # 각 8개 톱날과 자석 4개 / N극 0, S극 1


    # K번 실시
    for i in range(K):
        num,d = map(int,input().split())# 회전시키려는 자석의 번호, 회전방향(1 : 시계, -1 : 반시계)



        for r in range(1,5):


            lst = []
            for c in range(8):
                lst.append(matrix[r][c])

                # 시계 방향이면 idx +1씩 이동
                if d == 1:
                    x = lst.pop()
                    lst.insert(0,x)
                    if matrix[r][]


                # 반시계 방향이면 idx -1씩 이동
                elif d == -1:
                    y = lst.pop(0)
                    lst.append(y)

