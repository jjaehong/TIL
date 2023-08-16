
fibo = [1,1]

lst = [fibo.append(fibo[i-1]+fibo[i]) for i in range(1,9)]
print(fibo)