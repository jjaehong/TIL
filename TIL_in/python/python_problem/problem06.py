def caesar(word, num):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.

    lst = []
    for i in word:

        # ord(i) + num => 알파벳 ~에서 num만큼 민 결과물
        # ord(i) + num - ord('A') => A로부터 얼마만큼 떨어져있나
        # num이 26보다 크다면? => 다시 A로 돌아가야함.
        # 29번 미는거랑 3번 미는거랑 똑같다. num % 26
        # (ord(i) + num - ord('A')) % 26 => 이 식이.. z를 넘어가더라도 다시 A로 돌아와서 '얼마나 밀었냐'가 되어버림
        if i.isupper():
            temp = chr(ord('A') + (ord(i) + num - ord('A')) % 26) # 알파벳 ~과 밀은 횟수를 더한 것이 z를 넘어간다면 다시 A로 돌아와야함.
            lst.append(temp) 


        elif i.islower():
            temp = chr(ord('a') + (ord(i) + num - ord('a')) % 26)
            lst.append(temp)
            
    return ''.join(lst)


# 아래 코드는 실행을 위한 코드입니다.
if __name__ == "__main__":
    # 아래의 코드는 수정하지 마세요.
    print(caesar("ssafy", 1))  # => ttbgz
    print(caesar("Python", 10))  # => Zidryx
    # 아래에 추가 테스트를 위한 코드 작성 가능합니다.

