# 3<= N <= 100
# 맨 앞의 숫자를 맨 뒤로 보내기 : m번
# 수열의 맨 앞에 있는 숫자 출력

# 자리 바꾸면서?

# 재귀함수
# 맨 앞 -> 맨 뒤 (종료 조건)
# f

# 삽입 하나 하고 하나

def go_back():

    # 초기화
    size = N+M
    q = [0] * size
    front = rear = -1

    # q에 col원소들 삽입
    for i in range(N):
        rear += 1
        q[rear] = col[i]

    # 작업을 m번 시행
    for j in range(M):
        front += 1
        x = q[front]
        rear += 1
        q[rear] = x
        print(q)

    return q[front+1]




import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    col = list(map(int, input().split()))

    print(f' #{tc} {go_back()}')




