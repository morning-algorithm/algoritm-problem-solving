import sys
#sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline #입력량이 많을 때 입력 속도를 빠르게
# s = input().rstrip(); # 줄바꿈 문자를 제거한 문자열 읽기

def DFS(v):
    global cnt
    if v==k:
        for x in res:
            print(x, end=" ")
        print()
        cnt+=1
    else:
        for i in range(n):
            res[v]=i+1
            DFS(v+1)



if __name__=="__main__":
    n,k=map(int,input().split())
    res=[0]*k
    cnt=0
    DFS(0)
    print(cnt)