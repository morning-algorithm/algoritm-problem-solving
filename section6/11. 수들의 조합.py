import sys
#sys.stdin = open("input.txt","rt")

#me
n,k = map(int,input().split())
a = list(map(int,input().split()))
m = int(input())

def dfs(L,s): #s:가지리스트 중 뻗어나갈 수 있는 인덱스 중 제일 작은 인덱스
    global cnt
    if L == k:
        if sum(res) % m == 0:
            cnt += 1
        return
    for i in range(s,n):
        res[L] = a[i]
        dfs(L+1, i+1) #i+1이다 !! s+1이 아니라!!! 자기랑 같거나 작은 인덱스는 못 가므로 중복이 없다! 
    
cnt = 0
res = [0]*k
dfs(0,0)
print(cnt)

#answer
'''
dfs(L,s(가지 시작 인덱스), sum)
sum값을 마지막에 한번에 계산하지않고 dfs할때마다 더했음!
DFS(L+1, i+1 , sum+a[i])
'''
