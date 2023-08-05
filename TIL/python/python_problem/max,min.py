# 최대 최소값 구하기!
# 파이썬 내장함수 max, min 사용 금지
# float('inf') : 대소비교시 유용

def max_score(scores):
    pass
    # 여기에 코드를 작성합니다.
    maxi = -float('inf') # 초기 기준값 음 무한대 설정
    for i in scores:
        if maxi < i: # maxi와 i(요소) 중 더 큰 것을
            maxi = i # maxi로 바꿔준다.
        else:
            continue # 계속 maxi와 i(요소)를 비교하면서 최대값을 갱신한다.
    return maxi


if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    scores = [30, 60, 90, 70]
    print(max_score(scores)) # 30
    # 아래 부터 추가 예제 코드 작성 가능합니다.


# def min_score(scores):
#     pass
#     # 여기에 코드를 작성합니다.
#     mini = float('inf') # 초기 기준값 양 무한대 설정
#     for i in scores:
#         if mini > i: # mini와 i(요소) 중 더 작은 것을
#             mini = i # mini로 바꿔준다.
#         else:
#             continue # 계속 mini와 i(요소)를 비교하면서 최소값을 갱신한다.
#     return mini

# if __name__ == '__main__':
#     # 아래의 코드는 수정하지 않습니다.
#     scores = [30, 60, 90, 70]
#     print(min_score(scores)) # 30
#     # 아래 부터 추가 예제 코드 작성 가능합니다.
