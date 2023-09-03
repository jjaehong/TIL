# 정식이의 은행업무

import sys

sys.stdin = open('input.txt', 'r')

# 수 하나씩 반전시켜가며 2진수와 3진수가 일치하는 값을 찾자.
#

T = int(input())
for tc in range(1, T + 1):
    two = input()
    three = input()

    # 2진수 반전

    binary = int(two, 2)
    bin_list = [0] * len(two)

    for i in range(len(two)):
        bin_list[i] = binary ^ (1 << i) #



    print(bin_list)
