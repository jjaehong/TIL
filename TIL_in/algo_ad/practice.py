# 연습문제 3


# 0. 이진 트리 저장

    # 1차원 배열 저장

# 1. "연결" 리스트로 저장 : 개발용
class Treenode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
    # 삽입 함수
    def insert(self,childnode):
        
        # 왼쪽 자식이 없을 경우
        if not self.left:
            self.left = childnode
            return
        
        # 오른쪽 자식이 없을 경우
        if not self.right:
            self.right = childnode
            return

        return
    
    # 순회
    def preorder(self):

        # 아무것도 없는 트리를 조회할 때
        if self != None:
            print(self.value, end=' ')

            # 왼쪽 자식이 있다면 왼쪽 자식 조회
            if self.left:
                self.left.preorder()
            
            # 오른쪽 자식이 있다면 오른쪽 자식 조회
            if self.right:
                self.right.preorder()



# 짝수번째 idx -> 홀수번째 idx 연결
arr = [1,2,1,3,2,4,3,5,3,6]

# 이진트리 만들기        
nodes = [Treenode(i) for i in range(0,14)]
for i in range(0,len(arr),2):
    parentnode = arr[i]
    childnode = arr[i+1]
    nodes[parentnode].insert(nodes[childnode])

nodes[1].preorder



# 2. 인접 리스트로 저장


