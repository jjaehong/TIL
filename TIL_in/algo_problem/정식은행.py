# 정식이의 은행업무

'''
1
1010
212
'''

T = int(input())
for tc in range(1, T + 1):
    A = input()  # 2진수
    B = list(map(int, input()))  # 3진수

    N = len(A)  # 2진수 자릿 수
    M = len(B)  # 3진수 자릿 수

    answer = 0

    binary = int(A, 2)  # 정수로 변환
    bin_list = [0] * N  # 각 비트를 반전시킨 수 N개 저장

    # 각 비트를 반전시킨 2진수 만들기
    for i in range(N):
        bin_list[i] = binary ^ (1 << i) # 배타적 논리합 : T/F가 하나씩 나와야 전체 True
        # print(bin_list)

    # 3진수의 B[i]자리를 바꾼 숫자 만들기
    # i번째 숫자를 기준('012')으로 j번째 숫자와 비교하면서
    for i in range(M): # i번째는 바꿀 숫자 정하기
        num1 = 0  # (B[i]+1) % 3
        num2 = 0  # (B[i]+2) % 3
        for j in range(M):
            # i 와 j가 다르면 그대로 B[j], 3진수 한칸 밀어주고
            if i != j:
                num1 = num1 * 3 + B[j]
                num2 = num2 * 3 + B[j]
            # i 와 j가 같으면
            else:
                num1 = num1 * 3 + (B[j] + 1) % 3
                num2 = num2 * 3 + (B[j] + 2) % 3

        if num1 in bin_list:
            answer = num1
            break   # for i

        if num2 in bin_list:
            answer = num2
            break   # for i


    print(f'#{tc} {answer}')
