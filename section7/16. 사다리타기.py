import sys
from collections import deque
#sys.stdin = open("input.txt","rt")

#me
def dfs(x,y):
    if x == 0: #출발지 행에 도착하면
        print(y)
        sys.exit(0)
        
    for i in range(3):
        xx = x + dx[i]
        yy = y + dy[i]
        
        if 0<=xx<10 and 0<=yy<10 and a[xx][yy] == 1:
            a[xx][yy] = 0
            dfs(xx,yy)
    
        
a = [ list(map(int,input().split())) for _ in range(10)]
dx = [0, 0, -1 ]
dy = [1, -1, 0]

for c in range(10):
    if a[9][c] == 2:#목적지행
        dfs(9,c)
