import sys
#sys.stdin = open("input.txt","rt")

#me
'''
"그 구역의 위, 아래, 왼쪽, 오른쪽 중 더 높은 구역으로만 이동할 수 있도록 등산로를 설계" 문제를 잘못이해해서 조금 해멨다.
위아래 왼쪽오른쪽중 제일 높은 구역이라고 해석해버렸다, 생각해보니 그렇게하면 경우의수가 없는데..
'''

def dfs(i,j):
      global cnt
      
      if i == maxx and j == maxy:
            cnt +=1
            return

      tmp = []
      for k in range(4):
            x = i+dx[k]
            y= j+dy[k]
            if 0<=x<=n-1 and 0<=y<=n-1 and ch[x][y] == 0 and a[x][y] > a[i][j]: #그 구역의 위, 아래, 왼쪽, 오른쪽 중 더 높은 구역으로만 이동
                  ch[x][y] = 1
                  dfs(x,y)
                  ch[x][y] = 0

            
n = int(input())
minx = 0
miny = 0
maxx= 0
maxy = 0
dx = [ -1, 0, 1, 0]
dy = [0, 1, 0 , -1]
cnt = 0
ch = [[0]*n for _ in range(n)]

a = [ list(map(int,input().split())) for i in range(n)]
for i in range(n):
      for j in range(n):
            if a[maxx][maxy] < a[i][j]:
                  maxx= i
                  maxy = j
            if a[minx][miny] > a[i][j]:
                  minx= i
                  miny = j

ch[minx][miny] = 1
dfs(minx,miny)
print(cnt)

#answer
'''
출발, 목적지 좌표 구하는 것 빼고 미로탐색과 동일하다
'''
