############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum 함수를 사용하지 않습니다.
# 사용시 감점처리 되니 반드시 확인 바랍니다.
def sum_primes(number):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    result = 0

    # 소수인지 확인하려면 number -1 까지 다 나눠 보면 된다.
    # 2 부터 number -1 까지 나눠 봤는데 나머지가 0인적이 있었다 => 소수 아님
    # 0인 적이 없었으면 소수니까 합을 구하고.. (17은 제외)
    for num in range(2, number):
        is_prime = True  # 소수라고 가정후 시작

        if num == 17:  # 17은 제외
            continue

        for i in range(2, num):  # 나누어 떨어지는지 확인
            if num % i == 0:
                # 약수 i를 발견해버림 (num은 소수가 아님!!)
                is_prime = False  # num은 소수가 아니라고 체크
                break

        if is_prime:  # is_prime 이 처음 가정 그대로 소수인 경우만 합 구하기
            result += num

    return result


# 아래 코드는 실행을 위한 코드입니다.
if __name__ == "__main__":
    print(sum_primes(22))  # => 60
    print(sum_primes(33))  # => 143
    # 아래에 추가 테스트를 위한 코드 작성 가능합니다.
