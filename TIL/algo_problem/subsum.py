# 구간합 구하기
# 이 문제에서의 핵심은 연속된 숫자의 합을 for문으로 표현하는 것이었다.
              

import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    arr = list(map(int, input().split()))

    max_sum = 1
    min_sum = 10000 * M # M 곱하는 이유 : 최대값이 10000인데 원소 m개 만큼 더하니까 

    for i in range(N-M+1): # 10 5 => 6개의 구간합
        total = 0
        
        for j in range(M): # 각각의 구간합을 구해야됨.            
            total += arr[i+j] # i 위치에서 M개 골라서 합을 구함.

        max_sum = total if total > max_sum else max_sum
        min_sum = total if total < min_sum else min_sum


    print(f'#{tc} {max_sum - min_sum}')
