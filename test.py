a = [1, 2, [1, 2]]
b = a[:]
print(a, b)  # [1, 2, [1, 2]] [1, 2, [1, 2]]


b[2][0] = 100
b[0] = 20
a[1] = 50
print(a, b)  # [1, 2, [100, 2]] [1, 2, [100, 2]]