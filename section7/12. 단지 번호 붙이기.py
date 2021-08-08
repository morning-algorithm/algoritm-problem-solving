import sys
#sys.stdin = open("input.txt","rt")

def dfs(nowx,nowy,k):
    ch[nowx][nowy] = k #이 작업을 if문 안에서 해서 main을 for문을 통해 들어온 애들은 처리가 안됐었음!
    if k in b:
        b[k] += 1
    else:
        b[k] = 1
    for i in range(4):
        x = nowx + dx[i]
        y = nowy + dy[i]

        if 0<=x<n and 0<=y<n and a[x][y] == 1 and ch[x][y] == 0:
            dfs(x,y,k) #센곳 또 세면 안되니까 back할떄 체크 안풀기!
   
n = int(input())
a = [ list(map(int,list(input()))) for _ in range(n) ]
ch = [ [0]*n for _ in range(n) ]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
b = dict()
k = 0

for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and ch[i][j] == 0:
            k += 1
            dfs(i,j,k)

b = sorted(b.values())
print(len(b))
for value in b:
    print(value)

#answer
'''
dfs, bfs 둘다 풀 수 있음.
dfs 풀이:
    이중포문으로 갈 수 있는 곳 발견하면 dfs호출
    dfs 처음 호출하면 dfs로 퍼져나가면서 갈 수 있는 곳 모두 감.
    단지 갯수 따로 세고, 각 단지당 세대수도 따로 세줘야한다.
'''
