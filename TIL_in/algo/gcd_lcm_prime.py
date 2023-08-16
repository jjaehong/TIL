# 최대공약수 gcd : greatest common divisor

# 최소공약수 lcm : least common multile

# 최대공약수
# a > b

def gcd(a,b):
    for i in range(b,0,-1):
        if a % i == 0 and b % i == 0:
            return i # 뒤에서부터 나오니 공약수 중 가장 큰 값이 나옴


# 유클리드 호제법
# a > b
# a,b 의 최대공약수 구하기
# a와 b, a를 b로 나눈 나머지 r이 있다고 했을 때 다음이 성립한다.
# a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
# 재귀적으로 (a,b) == (b,r)
# new_gcd(a,b) == new_gcd(b,r)

def new_gcd(a,b):

    # 종료 조건
    if b == 0:
        return a
    # 재귀 호출
    else:
        return new_gcd(b, a % b) # a%b = r

# 최소공배수
# a 와 b의 최소공배수는
# a와 b의 곱을 a와 b의 최대공약수로 나눈 것과 같다.

def lcm(a,b):
    return a * b // new_gcd()

a = 20
b = 15
print(gcd(a,b))
print(lcm(a,b))



# 1과 자기 자신만을 약수로 가지는 수
# prime number

# 어떤 숫자 n이 소수인지 소수가 아닌지
# 1부터 n까지 다 나눠보고 나누어 떨어진 횟수가 2개보다 많으면
# 2부터 n-1까지 다 나눠보고 나누어 떨어진 적이 한번이라도 있으면
# 소수가 아니다


prime = []
for i in range(2,1000):
    # i가 소수인지 아닌지 판별
    # 소수이면 prime에 추가
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime.append(i)


"""
에라토스테네스의 체
체를 거르듯이 소수를 판별
2부터 소수를 구하고자 하는 구간의 모든 수를 나열
처음에 시작할때는 2부터 모든 수가 소수라고 생각
2부터 소수를 판별하기 시작하는데 2는 소수다.
소수인 수들은 자기 자신을 제외한 자기의 배수를 모두 소수가 아니라고 체크
다음 수로 이동(체크가 안되있는 수)
위의 과정을 계속 반복
"""

n = 1000 # 2부터 1000까지의 모든 수에 대하여 소수판별
is_prime = [True for i in range(n+1)] # is_prime[i] => 숫자 i가 소수인가? 소수면 True

for i in range(2, int(n**0.5) + 1):
    if is_prime[i]: # i가 소수인 경우
        # i를 제외한 모든 i의 배수를 소수가 아니라고 체크
        j = 2
        while i*j <= n:
            is_prime[i*j] = False
            j += 1

print(is_prime[29]) # 29가 소수냐?