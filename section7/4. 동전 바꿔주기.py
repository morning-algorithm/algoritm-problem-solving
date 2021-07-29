import sys
#sys.stdin = open("input.txt", "r")
#동전 구해주기
def DFS(L,sum):
    global cnt,pn
    if sum==T:
        cnt+=1
    elif sum>T or L==k:
        return
    else:
        for i in range(pn[L][1]+1):
            DFS(L+1,sum+pn[L][0]*(i)) # 동전의 갯수: 0 ~ pn[L][1]

if __name__=="__main__":
    T=int(input())
    k=int(input())
    pn=[] #동전의 금액과 개수
    for i in range(k):
        a,b=map(int, input().split())
        pn.append([])
        pn[i].append(a)
        pn[i].append(b)
    cnt=0
    DFS(0,0)
    print(cnt)