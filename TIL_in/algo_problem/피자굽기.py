T = int(input())
 
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cheeze = list(map(int, input().split()))
 
    # 다음에 꺼내올 피자 인덱스
    next_i = 0
 
    # 오븐을 큐로 만들어보자
    q = [0] * 1000
    front = rear = -1
 
    # 오븐의 크기만큼 피자 넣어주기
    for i in range(N):
        rear += 1
        q[rear] = [i, cheeze[i]]  # [피자 번호, 치즈 양]
        next_i += 1
 
    # 오븐에 남아있는 피자의 개수
    remain = N
    # 마지막에 꺼낸 피자의 번호
    last_idx = -1
 
    # 모든 피자의 치즈가 녹을때까지 반복
    while True:
        # 피자를 하나 꺼내서 치즈를 녹인다(c // 2)
        front += 1
        cheeze_idx, cheeze = q[front]
        cheeze //= 2
 
        # 남은 치즈 양이 0이 아니다 ==> 다시 오븐에 넣기
        if cheeze != 0:
            rear += 1
            q[rear] = [cheeze_idx, cheeze]  # [피자 번호, 피자 치즈]
 
        # 남은 치즈 양이 0이 되었다
        else:
            # 현재 오븐의 자리에 남은피자 하나 꺼내서 넣기
            if next_i < M:
                rear += 1
                q[rear] = [next_i, cheeze[next_i]]
                # 하나 꺼냈으니까 다음에 꺼내올 피자 번호 1 증가
                next_i += 1
             
            # 넣을 피자가 없다
            else:
                remain -= 1
                # 오븐에 남은 피자도 없는 상황이 온다
                if remain == 0:
                    # 현재 피자의 번호가 답이 된다.
                    last_idx = cheeze_idx
                    # 답을 구하고
                    # 반복 종료
                    break
 
    print(f"#{tc} {last_idx + 1}")


