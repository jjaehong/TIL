import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    r1,c1,r2,c2 = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    cnt = 0

    for r in range(r1,r2+1):
        for c in range(c1,c2+1):
            total += matrix[r][c]
            cnt += 1

    average = total//cnt

    result = 0
    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            for i in range(1000):
                if matrix[r][c] > average:
                    result += 1
                    matrix[r][c] -= 1
                elif matrix[r][c] < average:
                    result += 1
                    matrix[r][c] += 1
                else:
                    matrix[r][c]


    print(f'#{tc} {result}')
    print(matrix)



