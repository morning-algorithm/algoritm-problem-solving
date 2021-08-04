import sys
#sys.stdin = open("input.txt", "r")

def DFS(L,sum,time):
    global max
    if time>m:
            return
    if L==n:
        if max<sum:
            max=sum
    else:
        DFS(L+1,sum+ps[L],time+pt[L])
        DFS(L+1,sum,time)

if __name__=="__main__":
    n,m=map(int, input().split())
    ps=[]
    pt=[]
    max=0 #최대 점수
    for i in range(n):
        s,t= map(int, input().split()) # 점수, 걸린 시간
        ps.append(s)
        pt.append(t)
    DFS(0,0,0)
    print(max)