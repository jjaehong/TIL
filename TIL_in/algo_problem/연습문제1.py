# 연습문제 1
# 2진수 -> 10진수 : 방법 2가지


bit = "0000000111100000011000000111100110000110000111100111100111111001100111"
"정답 : 0 120 12 7 76 24 60 121 124 103"
n = len(bit)

# 0b : 이진수
# 0o : 팔진수
# 0x : 16진수  1:1, 2:2, .. 10 : A , 11 : B ... 15 : F => 1111
# 0xA == 10

# bin() : 2진수로 바꿔주는 함수
# hex() : 16진수로 바꿔주는 함수

# for i in range(0, n, 7):
#     bit7 = "0b" + bit[i: i + 7]
#     print(bit7)
#     dec = int(bit7, 2) # int(iterable,n) / n진수를 -> 10진수로 바꿔주기
#     print(dec, end=" ")
# print()

# 이진수를 7칸 쪼개서 십진수로 만들기
for i in range(0, n, 7):
    # i번째 비트부터 7칸
    bit7 = bit[i: i + 7]
    # print(bit7)
    base = 2  # 지수 밑
    ex = 0  # 거듭제곱
    dec = 0  # 십진수로 바꾼결과 (여기에 누적합)
    for j in range(6, -1, -1):
        if bit7[j] == '1':
            dec += (base ** ex)
        ex += 1
    print(dec, end=" ")
print()





