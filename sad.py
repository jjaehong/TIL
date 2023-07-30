

class Student:

    def __init__(self, name ,gender, height):
        self.__name = name
        self.__gender = gender
        self.__height = height

    @property # 어떤 인스턴스 변수에 대한 getter method를 의미함
    def name(self):
        return self.__name
    
    @property
    def gender(self):
        return self.__gender
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        self.__height = height

    def __repr__(self):
        return f'{self.__class__.__name__}(name : {self.name}, gender : {self.gender}, height : {self.height})'


students = [
    Student('승재홍', '남', 174),
    Student('이순신', '남', 188),
    Student('유관순', '여', 158),
    Student('강감찬', '남', 182),
]

for student in students:
    print(student) 

print("name으로 오름차순 정렬 후 ===> ")
for student in sorted(students, key=lambda x: x.name):
    print(student)


print("name으로 내림차순 정렬 후 ===> ")
for student in sorted(students, key=lambda x:x.name, reverse=True):
    print(student)

print("height로 내림차순 정렬 후 ===> ")
for student in sorted(students, key = lambda x:x.height):
    print(student)


    
    