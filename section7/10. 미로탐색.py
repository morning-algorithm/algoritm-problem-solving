import sys
#sys.stdin = open("input.txt","rt")

#me
def dfs(nowx,nowy):
      global cnt
      if nowx == 6 and nowy == 6:
            cnt +=1
            return

      for i in range(4):
            x = nowx+ dx[i]
            y = nowy + dy[i]

            if 0<=x<=6 and 0<=y<=6 and a[x][y] == 0 and ch[x][y] == 0:
                  ch[x][y] = 1
                  dfs(x,y)
                  ch[x][y] = 0
      


a = [ list(map(int,input().split())) for _ in range(7) ]
dx = [ -1, 0, 1, 0]
dy = [0, 1, 0, -1]
ch = [ [0]* 7  for _ in range(7) ]
cnt = 0
ch[0][0] = 1
dfs(0,0)
print(cnt)

#answer
'''
최단거리 문제x.
출발점에서 도착점까지 가는 경우의 수(가지수)를 구하는 것. => dfs!!
한곳으로 쭉 뻗어나가서 도착점까지 가고 back해서 다른길 찾아보고 하는 것이 dfs

호수에 물을 던졌을때 동심원이 계속 커지는 것: bfs
한 길로 쭈욱 뻗어나가다가 back하는 것: dfs

격자탐색 풀이:
      한 길로 계속 뻗어나감.
      지나온 길은 방문 안함
      도착점에 도착하면 **back. 이때 꼭 check를 풀어줘야함** 다른길로 왔을때 다시 방문할 수 있게끔!!!!
'''
