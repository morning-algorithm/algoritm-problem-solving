import sys
#sys.stdin = open("input.txt","rt")

#me
'''1번 노드에서 n번 노드로 가는 모든 경로의 가지수 출력'''
def dfs(i):
    global cnt
    
    if i == n:
        cnt += 1
        return
    
    for j in range(1,n+1):
        if g[i][j] == 1 and ch[j] == 0:
            ch[j]= 1 #방문 체크
            dfs(j)
            ch[j]= 0 #빽 할 때 꼭 체크 해제 !
            
n,m = map(int,input().split())
g = [[0]*(n+1) for _ in range(n+1)]
ch = [0]*(n+1)
s = []
cnt = 0

for _ in range(m):
    a,b = map(int,input().split())
    g[a][b] = 1

ch[1] = 1 
dfs(1)
print(cnt)

#answer
'''
한번 방문한 노드는 다시 방문하지 않도록 꼭 방문 체크 !!! 안그럼 무한정 왔다갔다 거림.
빽 할 때 꼭 체크 해제!

* 경로 까지 출력하려면
    path.append(j)
    ch[j]= 1
    dfs(j)
    ch[j]= 0
    path.pop()
'''
