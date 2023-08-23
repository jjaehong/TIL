
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N, hexa = input().split()
    
    # 16진수 -> 10진수
    dec = int(hexa,16)
    print(f'#{tc} {dec}')

    # 10진수 -> 2진수
    result = ""
    for i in range(len(hexa)*4): # 2진수의 자리 = 16진수의 자리 * 4
        if dec & (1 << i) == 0:
            result += "0"
        else:
            result += "1"

    print(f'#{tc} {result[::-1]}') # 뒤에서부터 출력


    

    
    


