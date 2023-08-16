# 문자열 비교
# 고지식한 패턴 매칭 알고리즘 사용해보기
# 구간합

import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for tc in range(1,T+1):
    pattern = input() # 내가 찾고자하는 패턴 문자열
    text = input() # 여기 안에서 찾고 싶다

    # text 안에 pattern이 있냐?
    # 있으면 1, 없으면 0 출력

    # 인덱스 활용하여 풀이
    # 패턴, 텍스트에서 비교할 문자의 위치
    pi = 0
    ti = 0
    answer = 0
    # 비교 시작
    # while 사용 이유 : text 길이와 pattern 길이가 매 tc마다 달라지기에
    # 비교할 문자의 위치가 문자열의 길이보다 길면 안되기 때문에
    while pi < len(pattern) and ti < len(text):

        # 현재 위치에서부터 비교를 시작한다.
        # 현재 위치 pi에 있는 문자와 ti에 있는 문자가 같으면
        # pi와 ti 1씩 증가해 가면서 계속 비교(끝 or 다른게 나올 때까지)
        if pattern[pi] == text[ti]:
            pi += 1
            ti += 1
        # 다르면 ti는 pi만큼 다시 앞으로 갔다가 다음 위치에서 비교를 해야하니까 1 증가
        # 구간합과 유사
        # pi는 0으로 바뀜
        else:
            ti = ti - pi + 1
            pi = 0
        # 패턴 문자의 위치 pi가 패턴의 길이만큼 되버렸다면
        # 그 전에 있던 모든 문자가 같았다는 의미이다.
        # 패턴을 발견했다는 것을 의미한다.

        if pi == len(pattern):
            answer = 1
        else:
            answer = 0

    print(f'#{tc} {answer}')