# filter(function, iterable)

# function의 결과는 True or False
# 결과가 True인 것들만 골라서 반환

# 리스트의 홀수만을 걸러내는 함수

def odd(n):
    return n % 2

numbers = [1,2,3,4,5]
new_numbers = list(filter(odd,numbers))

print(new_numbers)


new_numbers1 = list(filter(lambda n : n % 2, numbers))
print(new_numbers1)
