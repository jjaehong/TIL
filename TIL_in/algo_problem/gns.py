import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    t, n = map(str, input().split())
    strings = list(map(str, input().split()))
    
    # 외계어 값들 딕셔너리로 저장
    num_dict = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
    
    
    c = [0] * 10

    # 정렬 결과
    arr = [''] * int(n)
    
    # 순서대로 count정렬
    for i in range(int(n)):
        c[num_dict[strings[i]]] += 1

    # 누적합 = 자리 구하기
    for i in range(9):
        c[i+1] += c[i]
    
    # 뒤에서부터 숫자 삽입
    for i in range(int(n)-1,-1,-1):
        c[num_dict[strings[i]]] -= 1
        arr[c[num_dict[strings[i]]]] = strings[i]
 
    print(t)
    print(' '.join(arr))