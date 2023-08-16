lst = []
for i in range(5):
    num = int(input())
    lst.append(num) # 5개 입력받은 리스트 작성

sum = 0
for j in lst:
    sum += j

print(f'입력된 값 {lst}의 평균은 {sum/len(lst):.1f}입니다.')


# # total = sum(lst)
# # aver = total/len(lst)


# lst = []
# for i in range(5):
#     num = int(input())
#     lst.append(num)
 
# a = [j for j in lst]

# print(f'입력된 값 {lst}의 평균은 {sum(a)/len(lst):.1f}입니다.')