import sys
#sys.stdin=open("input.txt", "r")
#양팔 저울 DFS

def DFS(L,v,p):
    if 1<=v<=s:# 특정 무게의 물을 담는 경우
            ch[v-1]+=1
    if L==k:# 추를 모두 사용했다면 
        return
    else:
        for i in range(p,k):
            DFS(L+1, v+w[i], i+1)
            DFS(L+1, v-w[i], i+1)

if __name__ =="__main__":
    k=int(input()) # 추의 개수
    w=list(map(int, input().split()))
    s=sum(w) # 추 무게의 합
    ch=[0]*s
    DFS(0,0,0)
    cnt=0
    for x in ch:
        if x==0:
            cnt+=1
    print(cnt)
