import sys
from collections import deque 
#sys.stdin = open("input.txt","rt")

#me
def bfs(x,y):
    dq = deque()
    dq.append((x,y))
    while dq:
        now = dq.popleft()
        for i in range(8):
            xx = now[0] + dx[i]
            yy = now[1] + dy[i]
            if 0<=xx<n and 0<=yy<n and a[xx][yy] == 1:
                a[xx][yy] = 0
                dq.append((xx, yy))

n = int(input())
a = [ list(map(int,input().split())) for _ in range(n) ]
dx = [-1, 0, 1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1 , 1, -1]
cnt = 0

for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            a[i][j] = 0
            cnt += 1
            bfs(i,j)

print(cnt)

#answer
'''
단지번호 붙이기랑 똑같은데 bfs를 활용해서 푼것.
그냥 대각선도 더 탐색하고, 섬의 갯수만 세면 됨'''
