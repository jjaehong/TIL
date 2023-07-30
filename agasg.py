# ws_8_3.py

# 아래 클래스를 수정하시오.

# class Animal:
#     num_of_animal = 0
#     def __init__(self):
#         Animal.num_of_animal += 1
    

class Dog():
    sound = '멍멍'


class Cat():
    sound = '야옹'
    

class Pet(Dog, Cat):
     
    def __str__(self):
        print(f'애완동물은 {sound} 소리를 냅니다.')



ani = Pet()
print(ani)

## init은 무언가를 출력할때 필요
## 매직 메서드는 바로 init되고 