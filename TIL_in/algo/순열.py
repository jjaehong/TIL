numbers = [1,2,3,4,5]

n = len(numbers)

# 자기 자신도 바꾸는 것을 포함해야한다.
# 자리를 바꿀 수 있는 경우의 수 : 5


def perm1(i):

    # 종료조건
    if i == n:
        print(numbers)
        return
    
    # 재귀호출

    for j in range(i,n):
        numbers[i], numbers[j] = numbers[j], numbers[i]

        perm1(i+1)

        numbers[i], numbers[j] = numbers[j], numbers[i]

perm1(0)
    