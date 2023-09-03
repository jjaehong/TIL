# 새로운 불면증 치료법

# n, 2n, 3n, 4n....kn
# n의 각 자리 수를 누적, 리스트에 넣기 : 0~9 모두 나오는 경우에서의 kn는?(k의 최소) k나오면 break
#

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())

    # c = [i for i in range(1000000)] # 100만

    
    # tmp = []
    # for i in range(0,len(c),N): # n,2n,3n...
    #     tmp += [c[i]]
    



    check = [str(i) for i in range(10)]
    
    # check 계속 제거해서 체크가 빌때까지 돌려
    while check:
        
        cnt = 0

        k = 1
        tmp = []
        for i in range(1,k):
            tmp += [N * i]
            k += 1



        # tmp 안에 하나씩 검사
        for i in range(1,len(tmp)): 
            # 하나씩 tmp안의 문자열 하나씩 검사
            cnt += 1
            for j in str(tmp[i]):

                # j가 0~9 에 포함되면
                if j in check:
                    cp = check.remove(j) # check안의 j값을 제거
                    # print(cp)
                # 포함안되면 넘겨
                else:
                    continue
            
            if not len(check):
                    break
            
    print(f'#{tc} {tmp[cnt]}')


    # 새로운 불면증 치료법

T = int(input())
for tc in range(1,T+1):
    N = int(input())

    answer = 0

    check = [str(i) for i in range(10)]
    # [0,1,2,3,4,5,6,7,8,9]
    
    j = 1
    while check:

        N1 = N * j
        # print(N1)
        for i in str(N1):
            
            if i in check:
                check.remove(i)
            else:
                continue
        
        if not check:
            answer = N1
            break
                
        j += 1
    print(f'#{tc} {answer}')   



                # if result2 in '0123456789':
                #     break

    # print(f'{tc} {cnt}') 

    # for i in range(len(tmp)):
    #     for j in range(len(str(tmp[i]))): 
    #         result.append(tmp[i][j])
    
    # if i in '0123456789':
    #     break