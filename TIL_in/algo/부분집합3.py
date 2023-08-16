numbers = [1,2,3,4,5]

selected = [0] * 5
# selected[i] == 1 : 내가 i번째 원소를 부분집합에 포함 o
# selected[i] == 0 : 내가 i번째 원소를 부분집합에 포함 x

n = len(numbers)

# 만약 합이 x보다 작은 부분집합만 구해야 한다면?
x = 6


# 재귀함수로 부분집합 구하기

# i번째 원소를 부분집합에 포함할지 안할지를 결정해준다.
# n-1 번째 원소까지 하면 된다.
# n-1 번째 원소까지 완료한 경우 뒤로 돌아와서 내가 이전에 선택했다면
# 선택하지 않고 진행 ==> 반복


# 내가 i번째 원소를 선택 or 선택x 했던 상황에서 합을 기억

def subset(i,n,subsum):

    # 0. 다른 조건(최적화)
    if subsum > x:
        return # subsum의 합이 x보다 크면 더 이상 진행할 필요가 없어!

    # 1. 종료 조건
    if i == n:

        # n개의 원소에 대한 선택을 끝냈다.(부분집합에 넣던지 안넣던지, n-1번째 원소까지 선택했다.)
        temp = 0
        for j in range(n):
            if selected[j]:
                temp += numbers[j]
        print()
        
        # 합이 x이하인 부분집합만 출력
        if temp <= x:
            for j in range(n):
                if selected[j]:
                    temp += numbers[j]
            print()
        return 

    # 2. 재귀호출
    # i번째 원소를 선택하고 다음 i+1 번째 원소를 선택하러 가거나
    selected[i] = 1
    subset(i+1, n, subsum + numbers[i]) # i번째 원소를 선택했기에 subsum에 더해줘야한다.

    # i번째 원소를 선택하지 않고 다음 i+1 번째 원소를 선택하러 가거나
    selected[i] = 0
    subset(i+1, n, subsum)

subset(0,n,0)
# 결과 리뷰
# 1~5를 모두 선택한 것을 먼저 출력
# 뒤로 돌아와서 1~4