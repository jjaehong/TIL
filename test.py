# ws_7_4.py

# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return (self.width + self.height) * 2
    
    def print_info(self):
        info_list1 = [self.width, self.height, self.calculate_area(), self.calculate_perimeter()]
        info_list2 = ['Width', 'Height', 'Area', 'Perimeter']
        i = 0
        j = 0
        while i < len(info_list1):
            print(f'{info_list1[j]} : {info_list2[j]}')
            i += 1
            j += 1

shape1 = Shape(5, 3)

shape1.print_info()
