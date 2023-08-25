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



        
        

