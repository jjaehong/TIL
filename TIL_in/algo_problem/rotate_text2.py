

import sys
sys.stdin = open("input.txt", "r")


for tc in range(1,11):
    t_len = int(input())
    t_mat = [list(map(str, input())) for _ in range(8)]

    # 결과값
    result = 0 

    # 행,열 우선순회
    for i in range(8):
        for j in range(8-t_len+1):
            
            # t_len 길이만큼 뽑은 행, 열 출력
            word_row = '' 
            word_col = ''

            for k in range(t_len):
                word_row += t_mat[i][j+k]
                word_col += t_mat[j+k][i]
            
            # 뽑은 행, 열에서 회문검색 
            
            r_cnt = 0
            c_cnt = 0
            for v in range(t_len//2):
                if word_row[v] == word_row[t_len-1-v]: # 주의 : 여기서 바로 결과값을 카운트하면 첫시도에서 맞으면 바로 카운트됨
                    r_cnt += 1  # 따라서 중간저장소를 만들어서 카운트 해준 뒤 최종 판단이 된 값을 결과값에 다시 넣어줘야한다.

                if word_col[v] == word_col[t_len-1-v]:
                    c_cnt += 1

            if r_cnt == t_len//2:
                result += 1
            if c_cnt == t_len//2:
                result += 1

            
            
    print(f'#{tc} {result}')






