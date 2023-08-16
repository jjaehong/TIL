# while + pop() 이용 

lst = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]

sum = 0
while len(lst) > 0:
    a = lst.pop()
    if a >= 80:
        sum += a
    
print(sum)