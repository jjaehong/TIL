# 10진수(N) -> 2진수 : 12자리 이내 : 0.~ 13자리 이상 overflow
#

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = float(input())

    # 2진수 문자열
    bin_string = ''

    # shift 갯수 세기
    cnt = 0

    # N이 0이 되면 종료 / N => 0이 안되는 경우는 overflow
    while N > 0:

        # 종료 조건
        if cnt >= 13:
            bin_string = 'overflow'
            break

        # 10진수에 2를 곱하기 = 2진수도 왼쪽 한칸씩 shift하는 효과
        N *= 2

        cnt += 1

        if N >= 1:
            bin_string += '1'
            N = N - 1

        elif N < 1:
            bin_string += '0'

    print(f'#{tc} {bin_string}')