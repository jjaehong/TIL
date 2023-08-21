# subtree


# 이 문제에서는 전위순회, 중위순회, 후위순회 뭘 하든 똑같은 결과가 나옴

# 전위 순회(VLR)
def preorder(node):
    global cnt
    # v - l - r
    if node != 0:  # 노드가 있다면? ==>         if child_left[parent] == 0:
                                                # child_left[parent] = child
                                                # 0이면 자식을 넣는데, 0이 아니어야 순회를 할 수 있다!
        cnt += 1
        # print(node, end=" ")
        preorder(child_left[node])
        preorder(child_right[node])


# 중위 순회(LVR)
def inorder(t):
    global cnt
    # l - v - r
    if t:
        inorder(child_left[t])
        cnt += 1
        inorder(child_right[t])


# 후위 순회(LRV)
def postorder(node):
    global cnt
    # l - r - v
    if node:
        postorder(child_left[node])
        postorder(child_right[node])
        cnt += 1


import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())  # E : 간선의 개수, N : 루트노드
    tree = list(map(int, input().split()))

    # 부모노드 인덱스 기준으로 **트리 저장**
    child_left = [0] * (E + 2)
    child_right = [0] * (E + 2)

    for i in range(E):
        parent = tree[i * 2]
        child = tree[i * 2 + 1]

        # 왼쪽 자식이 비어있으면 왼쪽부터 추가
        if child_left[parent] == 0:
            child_left[parent] = child
        # 왼쪽 자식이 이미 있으면 오른쪽 자식으로 추가
        else:
            child_right[parent] = child



    # N을 루트 노드로 하는 서브트리의 노드 개수
    cnt = 0
    preorder(N)  # N번부터 전위순회하겠다.
    # inorder(N) # N번부터 중위순회하겠다.
    # postorder(N) # N번부터 후위순회하겠다.

    print(f'#{tc} {cnt}')
