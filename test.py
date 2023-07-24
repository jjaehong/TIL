numbers = [1,2,3]
numbers2 = [4,5,6]


# numbers.append(numbers2)
# print(numbers) # [1, 2, 3, [4,5,6]]

print(numbers.extend(numbers2))
print(numbers) #[1,2,3,4,5,6]