numbers = [1,2,3,4,5]
n = len(numbers)

def perm2(i,selected):
    global cnt
    cnt += 1

    # 종료조건
    if i == n:
        print(selected)

        return

    # 재귀호출
    

    for j in range(n):
        if numbers[j] not in selected:
            selected[i] = numbers[j] # 숫자에 중복이 없다는 가정하에 진행
            perm2(i+1,selected)
            selected[i] = 0

cnt = 0
print(f'{perm2(0, [0]*5)}', cnt)
