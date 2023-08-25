
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    read = [input() for _ in range(5)]

    q = []
    for r in range(5):
        for c in range(5):
            q.append(read[c][r])




            # if 0 <= r < 
 
            # if read[c][r] == None:
            #     continue
            # else:
            #     q.append(read[c][r])
                

    
    print(''.join(q))



