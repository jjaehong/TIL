# 별 찍기, f-string 응용

i = 4
while i > 0:
    
    print(f'{"*"*(2*i-1):^7}') # :^7 오른쪽으로 7칸 띄어쓰기
    i -= 1
    # print(f'{sum:>5}') :>5 왼쪽으로부터 5칸 띄어쓰기
    


