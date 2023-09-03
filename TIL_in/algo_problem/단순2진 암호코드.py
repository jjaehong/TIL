# 단순2진 암호코드

# 주어진 암호를 7자리씩 끊어서 리스트로 나타내기
# 7자리가 
# 끊어낸 암호 덩어리들에서 홀수번째와 짝수번째 구분하고 10진수로 표현
# (홀수번째 끼리 합 * 3) + (짝수번째 끼리 합) = 10의 배수냐?
# 올바른 암호코드라면 10진수형태 출력, 아니면 0 출력

dic = {'0001101' : 0,
         '0011001' : 1,
         '0010011' : 2,
         '0111101' : 3,
         '0100011' : 4,
         '0110001' : 5,
         '0101111' : 6,
         '0111011' : 7,
         '0110111' : 8,
         '0001011' : 9}

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    password = [list(map(int, input())) for _ in range(N)]


    
    
    # 7자리씩 쪼개어 리스트에 넣기
    lst = []
    for r in range(N):
        for c in range(0,len(password),7):
            bit7 = password[r][c:c+7]
            lst.append(bit7)
    print(lst)

    for i in range(len(lst)):
        if lst[i] == dic.keys():
            lst[i] = dic[i] 





            
            # print(dec)

            # for i in range(7):
            #     if bit7[i] and

        #     # 2진수 -> 10진수
        #     dec = 0  
        #     for j in range(6, -1, -1):
        #         if bit7[j] == 1:
        #             dec += 2 ** (6-j)
        # print(dec, end=" ")



        # for j in range(len(bit7)):
        #     if bit7[j] % 2:
                

            # else:
            #     bi
    


    
            # if bit7[0:3] == 0 and bit7[3:5] == 1 and bit7[5] == 0 and bit7[6] == 1:
            #     dec = 0
            # elif bit7[0:2] == 0 and bit7[2:4] == 1 and bit7[4:6] == 0 and bit7[6] == 1:
            #     dec = 1
            # elif bit7[0:2] == 0 and bit7[2] == 1 and bit7[3:5] == 0 and bit7[5:] == 1:
            #     dec = 2
            # elif bit7[0] == 0 and bit7[1:4] and bit7[5] == 0 and bit7[6] == 1:
            #     dec = 3
            # elif bit7[0] == 0 and bit7[1] and bit7[2:5] == 0 and bit7[5:]:
            #     dec = 4
            # elif bit7[0] == 0 and bit7[1:3] and bit7[3:6] == 0 and bit7[6] == 1:
            #     dec = 5
            # elif bit7[0] == 0 and bit7[1] and bit7[2] ==0 and bit7[3:]:
            #     dec = 6
            # elif bit7[0] == 0 and bit7[1:4] and bit7[4] ==0 and bit7[4:]:
            #     dec = 7
            # elif bit7[0] == 0 and bit7[1:3] and bit7[3] ==0 and bit7[4:]:
            #     dec = 8
            # elif bit7[0:3] == 0 and bit7[3] == 1 and bit7[4] ==0 and bit7[5:]:
            #     dec = 9






