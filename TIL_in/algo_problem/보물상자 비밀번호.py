# 보물상자 비밀번호
# 분할, q,

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    hexa = input()

    # 16진수 -> 리스트 넣기
    lst = []
    for i in range(N):
        lst += [hexa[i]]

    # 옮기고 4분할하여 생성가능한 수
    tmp = []
    # 옮기기
    for i in range(N):
        x = lst.pop(0)
        lst.append(x)

        # 4분할
        for j in range(0, N, N // 4):
            bit4 = lst[j: j + (N // 4)]
            tmp += [''.join(bit4)]
        # print(tmp)

    # 중복 제거, 16진수 -> 10진수, 내림차순
    answer = list(set(tmp))

    result = []
    for i in range(len(answer)):
        result += [int(answer[i], 16)]

    result.sort(reverse=True)

    print(f'#{tc} {result[K - 1]}')
    # print(result)
