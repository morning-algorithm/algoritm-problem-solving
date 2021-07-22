import sys
#sys.stdin = open("input.txt", "r")

def DFS(x):
    if x==n+1:
        for i in range(n):
            if ch[i]==1:
                print(i+1, end=" ")
        print()
    else:
        ch[x-1]=1
        DFS(x+1)
        ch[x-1]=0
        DFS(x+1)

if __name__=="__main__":
    n=int(input())
    ch=[0]*n
    DFS(1)