import sys
#sys.stdin = open("input.txt", "r")
#동전 구해주기
def DFS(L):
    global a,res
    if L==n:
        ch=max(res)-min(res)
        if ch<a:
            #중복 제거 방법
            tmp=set()
            for x in res:
                tmp.add(x)
            if len(tmp)==3:# 중복이 없는 경우
                a=ch
    else:
        for i in range(3):
            res[i]+=money[L]
            DFS(L+1)
            res[i]-=money[L]

if __name__=="__main__":
    n=int(input())
    money=[] #동전
    for i in range(n):
        money.append(int(input()))
    res=[0]*3
    a=2147000000
    DFS(0)
    print(a)