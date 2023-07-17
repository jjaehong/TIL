# a를 문자열로 받음
# 문자열 더하기한 것을 리스트로 받음
# 리스트 요소들을 sum()

a = input("ss : ")
b = a

aplus = []
for i in range(4):
    aplus.append(int(a))
    a = a + b
print(aplus)

print(sum(aplus))


# 반복문으로 리스트 받기