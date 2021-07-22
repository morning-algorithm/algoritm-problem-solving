import sys
# sys.stdin = open("input.txt", "r")
# 1~7 이진 트리 DFS-> 전위순회, 중위순회, 후위순회


def DFS(v):
    if v>n:
        return
    else:
        print(v,end=" ") #위치1 - 전위순회/2 - 중위 순회/3 - 후위 순회
        DFS(v*2) # 왼쪽 자식 노드
        DFS(v*2+1) # 오른쪽 자식 노드

if __name__=="__main__":
    n=7
    DFS(1)