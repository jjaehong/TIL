# dict 정렬하기
# value를 중심으로 dict 정렬하기

dict_data = {
    "TV": 2000000,
    "냉장고": 1500000,
    "책상": 350000,
    "노트북": 1200000,
    "가스레인지": 200000,
    "세탁기": 1000000,
}

result = sorted(dict_data.items(), key = lambda x: x[1], reverse=True) # value 정렬
# print(x)
for i,j in result:
    print(f'{i}: {j}')


# result2 = sorted(dict_data.items()) # 그냥 정렬하면 key를 기준으로 정렬
# print(result2)
# for i,j in result2:
#     print(f'{i}: {j}')



