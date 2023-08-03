T = int(input())
for tc in range(1,T+1):
    P, AK, BK = map(int, input().split()) # 페이지 수, A.key, B.key

    l = 1
    r = P

    while l <= r:
        c = int((l+r)/2)
        if AK == c:
            print('A')
        elif BK == c:
            print('B')
        
        elif AK < c or BK < c:
            r = c-1

        elif AK > c or BK > c:
            l = c + 1
    print(0) 






