# 언패킹 이해하기

lst = [0,1,2,3,4,5,6,7,8,9]
ans = [0,0,0,0,0,0,0,0,0,0]

N = input()

for i in N:
    ans[int(i)] += 1 


print(*lst)
print(*ans)