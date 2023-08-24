hex1 = '0F97A3'
hex2 = '01D06709861D69F99F'

def solution(hex_string):
    # hex_string : 16진수 문자열
    # 이걸 2진수 문자열로 바꾸면 길이 * 4
    l = len(hex_string) * 4

    # 16진수 문자열을 숫자로 바꾸기
    x = int(hex_string, 16)
    # print(x)

    # 이진수로 바꾼 결과 문자열
    bin_string = ''

    # 7칸씩 잘라서 이진수로 만든 뒤에 이진수 출력
    # 그 이진수를 10진수로 바꾸고 출력
    

    for i in range(0,l,7):
        bit7 = str(x)[i:i+7]
        print(bit7)





solution(hex1)
'''

'''

solution(hex2)