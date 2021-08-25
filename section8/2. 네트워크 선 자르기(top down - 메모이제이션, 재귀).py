import sys
sys.stdin = open("input.txt", "r")

def DFS(len):
    if dy[len]>0:# 메모이제이션. 중복 재귀 X
        return dy[len]
    if len==0 or len==1:
        return len+1
    else:
        dy[len]=DFS(len-1)+DFS(len-2)
        return dy[len]

if __name__=="__main__":
    n= int(input())
    dy=[0]*n # 메모이제이션 구현  
    print(DFS(n-1))
