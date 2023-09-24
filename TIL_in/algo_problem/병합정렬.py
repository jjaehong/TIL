

# 병합 함수
def merge(left, right):

    # 왼쪽과 오른쪽을 합친 결과
    result = [0] * 100
    front = rear = -1
    global cnt
    cnt = 0
    # i, j :
    # i => 왼쪽 리스트에서 원소를 꺼낼 위치,
    # j => 오른쪽 리스트에서 원소를 꺼낼 위치


    # 왼쪽과 오른쪽 둘중에 하나라도 원소가 남아있으면 병합 진행
    while len(left) > 0 or len(right) > 0:

        if left[N//2] > right[N//2]:
            cnt += 1

        # 둘 다 원소가 남아있으면 누구꺼를 꺼내올건지 비교
        if len(left) > 0 and len(right) > 0:
            # 왼쪽의 맨 앞 원소가 오른쪽의 맨 앞 원소보다 작으면 왼쪽 맨앞 넣기
            if left[0] <= right[0]:
                rear += 1
                result[rear] = left[rear]
            # 그게아니면 오른쪽 맨앞 넣기
            else:
                rear += 1
                result[rear] = right[rear]

        # 왼쪽만 남아있으면 왼쪽 남은거 다 추가
        elif len(left) > 0:
            rear += 1
            result[rear] = left[rear]

        # 오른쪽만 남아있으면 오른쪽 남은거 다 추가
        elif len(right) > 0:
            rear += 1
            result[rear] = right[rear]

    return result

# 분할 정복 함수
def merge_sort(lst): # lst : 정렬할 리스트

    # 종료 조건 (더이상 분할 못할때 까지)
    if  N == 1:
        return lst

    # 분할
    mid = N // 2
    left, right = lst[:mid], lst[mid:]

    # 정복
    left = merge_sort(left)  # 왼쪽 정렬
    right = merge_sort(right)  # 오른쪽 정렬

    # 병합
    return merge(left, right)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    L = list(map(int,input().split()))

    merge_sort(L)

    print(f'#{tc} {L[N//2]} {cnt}')
