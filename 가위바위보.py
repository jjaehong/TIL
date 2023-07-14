# 가위바위보 게임

## com = 컴퓨터가 낼 가위바위보 중 하나 (할때마다 바뀐다)

# 조건문을 사용해서
# 누가 이겼는지 판별한 후에
# 승자를 출력
# 게임의 결과도 출력
# ex) 내가 가위를 내고 컴퓨터가 바위를 내서 패배하였습니다.
# ex) 내가 가위를 내고 컴퓨터가 보를 내서 승리하였습니다
import random

user = input("뭐 낼거야? : ")
print("내가", user)

nocs = ["가위", "바위", "보"]
com = random.sample(nocs,1)
print("컴퓨터가", com)

## sample과 choice의 차이 => 샘플은 여러개를 뽑을 수 있고 리스트로 받음. 초이스는 하나만 그냥 받음

# 유저가 가위일 때, 
if user == '가위':
    if com[0] == nocs[0]:
        print("비겼다.")
    elif com[0] == nocs[1]:
        print("졌다..")
    elif com[0] == nocs[2]:
        print("이겼다!")
# 유저가 바위일 때,
if user == '바위':
    if com[0] == nocs[0]:
        print("이겼다!.")
    elif com[0] == nocs[1]:
        print("비겼다.")
    elif com[0] == nocs[2]:
        print("졌다..")
# 유저가 보 일때,
if user == '보':
    if com[0] == nocs[0]:
        print("졌다..")
    elif com[0] == nocs[1]:
        print("이겼다!")
    elif com[0] == nocs[2]:
        print("비겼다.")


---

user = input("뭐 낼거야? : ")
print("내가", user)

nocs = ["가위", "바위", "보"]
com = random.choice(nocs)
print("컴퓨터가", com)

# 유저가 가위일 때, 
if user == '가위':
    if com == nocs[0]:
        print("비겼다.")
    elif com == nocs[1]:
        print("졌다..")
    elif com == nocs[2]:
        print("이겼다!")
# 유저가 바위일 때,
if user == '바위':
    if com == nocs[0]:
        print("이겼다!.")
    elif com == nocs[1]:
        print("비겼다.")
    elif com == nocs[2]:
        print("졌다..")
# 유저가 보 일때,
if user == '보':
    if com == nocs[0]:
        print("졌다..")
    elif com == nocs[1]:
        print("이겼다!")
    elif com == nocs[2]:
        print("비겼다.")
