# 딕셔너리 내포
# 공백제거하면서..
# output => {'apple': 5, 'banana': 6, 'melon': 5}

fruit = ['   apple    ','banana','  melon']

new_fruits= {fruit[i].strip(): len(fruit[i].strip()) for i in range(0,3)}
print(new_fruits)

# for i in range(0,3):
#     print(f'{fruit[i].strip()}: {len(fruit[i].strip())}')

