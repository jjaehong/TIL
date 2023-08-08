# 글자수
# 요구역량 : 문자열에서 count와 max_cnt / for문의 이해도(초기화, 저장값을 어디에 둬야할 지, 어떻게 맞출 지)
# 스토리
# str1의 요소와 str2의 요소가 같으면 각각 cnt += 1하며 저장,
# 각각 cnt를 비교하여 max_cnt를 찾자!

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    # 결과값
    max_cnt = 0

    for i in str1:

        cnt = 0 # 중간저장소 # i에 대한 cnt니까 i바로 밑에! # str1의 원소 중 같은 것들을 cnt에 저장
        for j in str2:
            if i == j:
                cnt += 1

        max_cnt = cnt if max_cnt < cnt else max_cnt # cnt 변수를 받아야 하니 그거에 맞춘

    print(f'#{tc} {max_cnt}')



