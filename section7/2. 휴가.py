import sys
#sys.stdin = open("input.txt", "r")

def DFS(L,sum):
    global max
    if L==n:
        if max<sum:
            max=sum
    else:
        if L+ps[L]<=n: # n일을 넘지 않는 경우
            DFS(L+ps[L],sum+pp[L])
        DFS(L+1,sum)

if __name__=="__main__":
    n=int(input())
    ps=[]
    pp=[]
    max=-2147000000 #int형 최솟값
    for i in range(n):
        s,p= map(int, input().split()) 
        ps.append(s)
        pp.append(p)
    DFS(0,0)
    print(max)