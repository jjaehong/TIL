# 홀수 구하기 + print방식

a = []
for i in range(1,100,2):
        a += [str(i)]
print(', '.join(a))




# 7의 배수이지만 5의 배수는 아닌 것들 출력

lst = []
for i in range(1,201):
    if i % 7 == 0 and i  %5 != 0:
        lst += [str(i)]
print(','.join(lst))


