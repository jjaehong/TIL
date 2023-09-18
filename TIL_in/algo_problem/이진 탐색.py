T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    A = list(map(int,input().split())) # n개
    B = list(map(int,input().split())) # m개

    A.sort()


    cnt = 0


    for num in B:

        left = 0 
        right = n-1

        while left <= right:

            mid = (left + right)//2

            if A[mid] == num:
                cnt += 1
                break   
            

            elif A[mid] > num :
                right = mid - 1


            else:
                left = mid + 1