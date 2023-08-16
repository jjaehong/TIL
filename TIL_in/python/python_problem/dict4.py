# 합집합과 딕셔너리 내포

a = {'아메리카노': 1900, '카페모카': 3300, '에스프레소': 1900, '카페라떼': 2500, '카푸치노': 2500, '바닐라라떼': 2900}
b = {'헤이즐럿라떼': 2900, '카페모카': 3300, '밀크커피': 3300, '아메리카노': 1900, '샷크린티라떼': 3300}

dict_data = a|b

# a.update(b)

result = {(i,j) for i,j in dict_data.items() if j >= 3000}
print(result)

# new_dict = {}
# for i,j in dict_data.items():
#     if j >= 3000:
#         new_dict[i] = j
#     else:
#         continue
# print(new_dict)
    
