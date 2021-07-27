import sys
sys.stdin=open("input.txt", "r")

def DFS(L,v):
    global cnt
    if L==k:
        if sum(res)%m==0:
            cnt+=1
    else:
        for i in range(v,n):
            res[L]=a[i]
            DFS(L+1,i+1)
            res[L]=0

if __name__=="__main__":
    n,k=map(int, input().split())
    a=list(map(int, input().split()))
    res=[0]*k
    m=int(input())
    cnt=0
    DFS(0,0)
    print(cnt)
