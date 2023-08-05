# 주어진 리스트에서 각 자리 숫자가 모두 짝수일 때 출력

x = [i for i in range(100,301)]

# 1번 인덱스 + 리스트이후 join()활용 # join은 str만 취급
lst = []
for i in x:
    if int(str(i)[0]) % 2 == 0 and int(str(i)[1]) % 2 == 0 and int(str(i)[2]) % 2 == 0 :
        lst += [str(i)]

print(','.join(lst))
# print(*lst)




# # 2번 //활용 + 마지막 값 전까지만 출력 후 마지막 값 합치기
# for i in range(100,301):
#     if i == 288: print(i)
#     elif i % 2 == 0 and (i//10) % 2 == 0 and (i//100) % 2 == 0:
#         print(i, end=",")
 


# 3번 //활용 + 문자열 슬라이싱 활용 출력

# result = ''
# for i in range(10,30):
    
#     if i % 2 == 0 and (i//10) % 2 == 0 and (i//100) % 2 == 0:
#         result += str(i) +","

# print(result[:-1])