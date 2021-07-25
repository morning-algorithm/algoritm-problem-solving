import sys
#sys.stdin = open("input.txt", "r")

def DFS(L):
    global cnt
    if L==k:
        for x in res:
            print(x, end=" ")
        cnt+=1
        print()
    else:
        for i in range(n):
            if ch[i]!=1:# 중복 방지
                res[L]=i+1
                ch[i]=1
                DFS(L+1)
                ch[i]=0

if __name__=="__main__":
    n,k=map(int, input().split())
    ch=[0]*n # 1-n까지의 숫자 확인
    res=[0]*k # 순열 결과
    cnt=0 # 순열의 개수
    DFS(0)
    print(cnt)