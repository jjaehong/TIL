# main.py

# 아래 함수를 수정하시오.
def find_min_max(lst):
    minimum = min(lst)
    maximum = max(lst)
    return minimum, maximum

result = find_min_max([3, 1, 7, 2, 5])
print(tuple(result)) # (1, 7)
