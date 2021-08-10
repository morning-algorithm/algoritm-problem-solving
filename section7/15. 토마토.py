import sys
from collections import deque
#sys.stdin = open("input.txt","rt")

#me
'''
bfs설계자체를 생각을 잘못했음. 4,5번에서 time limit가 나옴
def bfs(x,y):
    day = 2
    q = deque()
    q.append((x,y))
    while q:
        now = q.popleft()
        for i in range(4):
            xx = now[0] + dx[i]
            yy = now[1] + dy[i]
            day = a[now[0]][now[1]] + 1
            if 0<=xx<r and 0<=yy<c and ( a[xx][yy] == 0 or a[xx][yy] > day ):
                a[xx][yy] = day
                q.append((xx,yy))
        
c,r = map(int,input().split())
a = [ list(map(int,input().split())) for _ in range(r)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


for i in range(r):
    for j in range(c):
        if a[i][j] == 1:
            bfs(i,j)

max = -10
for i in range(r):
    for j in range(c):
        if a[i][j] == 0:
            print(-1)
            sys.exit(0)
        if max<a[i][j]:
            max = a[i][j]

print(max-1)
'''

#answer
'''
트리(시작점)가 여러개인 bfs.
먼저 제일 처음, 익은것들을 큐에 넣는다.
그리고 큐에서 하나씩 차례로 빼서 먼저 익은것 부터 퍼져나간다.
안익은 놈들을 골라서 익었다고 큐에 넣고 익었다고 표시를 1로 바꿔주고 그리고 dis 배열을 써서 시작점으로 부터 거리를 써준다.

bfs는 당연히 최단거리. 가장 가까운 익은곳으로 부터 거리가 써져야한다.
'''
c,r = map(int,input().split())
a = [ list(map(int,input().split())) for _ in range(r)]
dis = [ [0]*c for _ in range(r)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque()


# 시작점이 여러개 !!!!
for i in range(r):
    for j in range(c):
        if a[i][j] == 1:
            q.append((i,j))

#이제 시작점들이 준비되었으니 bfs
while q:
        now = q.popleft()
        for i in range(4):
            xx = now[0] + dx[i]
            yy = now[1] + dy[i]
            if 0<=xx<r and 0<=yy<c and a[xx][yy] == 0:
                a[xx][yy] = 1
                q.append((xx,yy))
                dis[xx][yy] = dis[now[0]][now[1]] + 1

max = -10
for i in range(r):
    for j in range(c):
        if a[i][j] == 0:
            print(-1)
            sys.exit(0)
        if max < dis[i][j]: #만약 처음부터 다 1인경우엔 dis가 전부 0이므로 0출력
            max = dis[i][j]

print(max)
