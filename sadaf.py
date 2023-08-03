# 연습문제 2
'''
3
19 6 16 19 15 16 8 13 16 10
-20 -6 -13 3 -19 -9 19 -3 9 4
7 7 19 1 -18 5 -9 -11 19 18
'''
T = int(input())
for tc in range(1, T+1):
    subset = list(map(int, input().split()))

    n = len(subset)
    
    
    for i in range(1<<n):

        sum = 0     
        for j in range(n):
            if i & (1<<j):
                sum += subset[j]
        
        if sum == 0:
            print('1')