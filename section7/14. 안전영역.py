import sys
from collections import deque 
#sys.stdin = open("input.txt","rt")

#me
def bfs(x,y,h):
    dq = deque()
    dq.append((x,y))
    
    while dq:
        now = dq.popleft()
        
        for i in range(4):
            xx = now[0] + dx[i]
            yy = now[1] + dy[i]
            
            if 0<=xx<n and 0<=yy<n and a[xx][yy] > h and ch[xx][yy] == 0:
                ch[xx][yy] = 1
                dq.append((xx, yy))

n = int(input())
a = [ list(map(int,input().split())) for _ in range(n) ]
ch = [ [0]*n for _ in range(n) ]
m = max(map(max,a)) #최대값 찾기
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = []
cnt = 0


for h in range(1,m):
    ch = [ [0]*n for _ in range(n) ]
    cnt = 0
    
    for i in range(n):
        for j in range(n):
            if a[i][j] > h and ch[i][j] == 0:
                cnt += 1
                ch[i][j] = 1 
                bfs(i,j,h)
    res.append(cnt)
print(max(res))


#answer
'''
bfs라고 명시해놓았지만 단지 찾기같은 문제는 dfs, bfs 뭘로하든 상관없다

풀이:
행을 탐색하다가 4보다 큰 숫자를 발견하면 연결된 4보다 큰 숫자가 있는 곳으로만 뻗어나감.그게 계속 뻗어나가면 하나의 영역이됨.
그리고 안전영역 문제는 for문을 여러번 돌아야하기 때문에 지도자체를 바꿔버리면 안되고 ch 배열을 새로 만들어야함.
백준사이트에서 채점받으려면 1~m까지 세는게 아니라 0~m까지 세야함.
백준사이트 같은 곳에서 재귀함수 돌리려고 할때 시간제한 `sys.setrecursionlimit(10**6)` 넣어야한다.
데이터 많고 타이트하게 시간제한 있을때 넣어야지 runtime error안난다!
'''
