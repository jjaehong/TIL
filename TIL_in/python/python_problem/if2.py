# 약수/소수 구하기


N = int(input())
cnt = 0

for i in range(1,N+1):
    if N % i == 0:
        print(f'{i}(은)는 {N}의 약수입니다.')
        cnt += 1

    if cnt == 2:
        print(f'{N}(은)는 1과 {N}로만 나눌 수 있는 소수입니다.')