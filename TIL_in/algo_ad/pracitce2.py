
arr = [1,2,1,3,2,4,3,5,3,6]



# 이진트리 만들기        
nodes = [ [] for _ in range(0,14)]
for i in range(0,len(arr),2):
    parentnode = arr[i]
    childnode = arr[i+1]
    
    nodes[parentnode].append(childnode)
    
    nodes[childnode].append(parentnode)


# 자식이 더 이상 없다는 것을 표현하기 위해 None을 삽입

for li in nodes:
    for _ in range(len(li),2):
        li.append(None)


def preorder(nodenumber):
    if nodenumber == None:
        return
    
    # print(nodenumber, end = ' ')
    preorder(nodes[nodenumber][0])
    # print(nodenumber, end = ' ')
    preorder(nodes[nodenumber][1])
    # print(nodenumber, end = ' ')

preorder(1)