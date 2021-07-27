import sys
#sys.stdin=open("input.txt", "r")

def DFS(v):
    global cnt
    if v==1:
        cnt+=1
    else:
        for i in range(n):
            if arr[i][v-1]==1 and ch[i]==0:
                ch[i]=1
                DFS(i+1)
                ch[i]=0


# 인접 행렬 (가중치 방향 그래프)
if __name__=="__main__":
    n,k= map(int, input().split())
    arr=[[0]*n for _ in range(n)]
    ch=[0]*n
    cnt=0
    for i in range(k):
        a,b=map(int, input().split())
        arr[a-1][b-1]=1

    DFS(n)
    print(cnt)