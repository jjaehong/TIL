import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    while N > 1 : 

        if N % 2 == 0 : # N이 2로 나눠지면
            N = N/2 # 2로 나눈 것을 다시 N으로 저장하고
            a += 1 # 소인수 1개 카운트
        
        elif N % 3 == 0:
            N = N/3
            b += 1

        elif N % 5 == 0:
            N = N/5
            c += 1
            
        elif N % 7 == 0:
            N = N/7
            d += 1

        elif N % 11 == 0:
            N = N/11
            e += 1

        if N == 0:
            break


    
    print(f'#{tc}',a,b,c,d,e)




