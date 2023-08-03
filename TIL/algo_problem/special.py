T = int(input())
for tc in range(1,T+1):
    n =int(input())

    numbers = list(map(int, input().split()))

    # 최대값 or 최소값의 위치(인덱스)
    idx = 0

    # 선택정렬
    for i in range(10):
        # i 위치에 올 원소를 찾아야합니다.

        
        # i 뒤에 있는 원소부터 찾기 시작
        for j in range(i, n):
            pass
            # i가 짝수일때 => 최대값 idx


            # i가 홀수일때 => 최소값 idx


    # 최대값 or 최소값 인덱스
    # i번째 원소는 누가 되야할까?? idx번째랑 자리를 교환

# numbers를 앞에서부터 10개만 출력
