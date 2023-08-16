# 테네스의 특별한 소수

# for + else

# 스토리 :
# A~B 범위 내에 소수 구하기
# 소수 중에 특별한 소수를 구하기

import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for tc in range(1, T + 1):
    D,A,B = map(int, input().split())


    # prime = []
    # for i in range(A, B+1):
    #
    #     for j in range(2, i):
    #         if i % j == 0:
    #             # 소수가 아니다.
    #             break # 나눠지는 게 있으면 종료
    #     else:
    #         prime.append(i)

    is_prime = [True for i in range(B+1)]

    for i in range(2, int(B**0.5) + 1):
        if is_prime[i]:
            j = 2
            while i*j <= B:
                is_prime[i*j] = False
                j += 1

    cnt_lst = []
    for j in range(2, len(is_prime)):
        if is_prime[j]:
            cnt_lst.append(j)

    cnt = 0
    for k in cnt_lst:
        for l in k:
            if D == k:
                cnt += 1

    print(f'#{tc} {cnt}')

    #
    #
    #     k
    # if cnt_lst
    #
    # print(cnt_lst)
    # #
    # #     if j == True:
    # #         cnt += 1
    # #
    # #     for k in str(j):
    # #         if D == int(k):
    #             cnt += 1
    #


