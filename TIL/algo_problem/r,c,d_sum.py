# sum


import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    max_row = 0
    max_col = 0
    dia1_tot = 0
    dia2_tot = 0

    for r in range(100):
        row_tot = 0
        col_tot = 0
        dia1_tot += matrix[r][r]
        dia2_tot += matrix[r][99-r]


        for c in range(100):
            row_tot += matrix[r][c]
            if max_row < row_tot:
                max_row = row_tot

            col_tot += matrix[c][r]
            if max_col < col_tot:
                max_col = col_tot
    


    result = [max_row, max_col, dia1_tot, dia2_tot]
    result.sort()

    print(f'#{tc} {result[3]}')


        







