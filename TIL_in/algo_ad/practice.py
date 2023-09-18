def partition(A, left, right):
    # 1. 피봇 정하기(제일 왼쪽 부분)
    p = A[left]

    # 2. 피봇 기준 분리 : 피봇보다 작은거는 왼쪽부터 놓고, 큰거는 오른쪽부터 놓고
    i, j = left, right
    # i : 왼쪽에 있으면 안되는 원소의 위치를 찾는 인덱스
    # 피봇보다 큰 원소의 위치 왼쪽 부터 찾기
    # j : 오른쪽에 있으면 안되는 원소의 위치를 찾는 인덱스
    # 피봇보다 작은 원소의 위치를 오른쪽 부터 찾기

    # 피봇보다 큰거를 왼쪽부터 찾기 시작
    while i <= j:
        # i번째 위치에 있는 원소가 피봇보다 작으면 오른쪽으로 한칸 가서 찾기 계속
        while i <= j and A[i] <= p:
            i += 1

        while i <= j and A[j] >= p:
            j -= 1

        if i < j:
            A[i], A[j] = A[j], A[i]

    A[left], A[j] = A[j], A[left]

    return j


# A : 정렬할 대상 리스트
# left : 왼쪽 인덱스
# r : 오른쪽 인덱스


def quick_sort(A, left, right):
    if left < right:
        pivot = partition(A, left, right)
        quick_sort(A, left, pivot - 1)
        quick_sort(A, pivot + 1, right)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    quick_sort(arr, 0, N - 1)
    answer = arr[(N // 2)]

    print(f"#{tc} {answer}")


"""
2
5
2 2 1 1 3
10
7 5 4 1 2 10 3 6 9 8

"""
