# flatten

dump = 70
box_height = [1m2m3m4m]

max_height = 1
min_height = 100

for height in box_heights(): # 박스 높이

            if max_height < height:
                max_height = height
        
            if min_height > height:
                min_height = height
            else:
                continue

            while dump == 0 or max_height == min_height :
                max_height -= 1
                min_height += 1
                dump -= 1