# 회문
# 요구역량
# 스토리 :

# 문자열 만들 공간 위치 지정 : 길이가 m인 문자열을 행 우선순회한다.(주의 : n,m이 다를 때)
# 문자열 만들기 : 시작지점 : (i,j)
# 회문검사 : (m 내부에서 각각 인덱스를 바꿨을 때도 같아야 함)

# 열 우선순회
# 회문검사


import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())

    # 글자모음(2차원 배열로)
    text = [list(input()) for _ in range(n)]

    # 우리가 찾는 회문
    answer = ''

    # 행 우선순회
    for i in range(n):
        for j in range(n-m+1): # 문자열 만들 공간 위치 지정
            # (i,j) 위치에 있는 글자부터 회문을 만들기 시작
            # 회문의 길이가 m이니까 (i,j) ~ (i,j+m) 까지의 글자를 모아서
            # 문자열로 만들면 완성 = > 이 문자열이 회문인지 아닌지 검사
            # j의 범위 주의!! (인덱스 범위 벗어나지 않도록)

            # (i, j) 위치에서 문자열 만들기 시작
            word_row = ''
            # 글자 m개 모아서 문자열 만들기
            for k in range(m):
                word_row += text[i][j+k]
            # print(word_row)
            rotate = 1
            for v in range(m//2):
                if word_row[v] != word_row[m-1-v]:
                    rotate = 0
            if rotate == 1:
                answer = word_row
            # word_row가 회문인지 아닌지 판별(인덱스 연산)
            # word_row가 회문이다 ==> answer = word_row

    # 열 우선순회(해보기)
    for j in range(n):
        for i in range(n-m+1):
            # 문자열 만들기 : 시작지점 : (i,j)
            word_col = ''
            for k in range(m):
                word_col += text[i+k][j]

            # 회문검사
            rotate = 1
            for v in range(m//2):
                if word_col[v] != word_col[m-1-v]:
                    rotate = 0
            if rotate == 1:
                answer = word_col

    print(f'#{tc} {answer}')







