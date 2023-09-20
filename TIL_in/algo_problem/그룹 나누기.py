

def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])

# 부모 통일
def union(x,y):
    # x집합의 대표와 y집합의 대표를 찾기
    x = find_set(x)
    y = find_set(y)

    if x > y:
        p[y] = x
    else:
        p[x] = y
        # 만약 두 집합의 깊이가 같은 경우, 깊이 + 1 증가
        if x == y:
            y += 1
    return x,y
    


T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split()) # 사람 수 : n명 / 신청서 수: m개
    arr = list(map(int, input().split()))


    # 전체 몇개의 조? == 총 대표가 몇명??
    cnt = 0

    # 집합 초기화
    p = [0] * (N+1)
    for i in range(1,N+1):
        p[i] = i
    
    # 집합 통일
    for i in range(M):
        union(arr[2*i],arr[2*i+1])
        






    print(p)
    answer = list(set(p))
    print(answer)


    

    # print(f'#{tc} {cnt}')

        

    



'''
3
5 2
1 2 3 4
5 3
1 2 2 3 4 5
7 4
2 3 4 5 4 6 7 4

'''

    




    
