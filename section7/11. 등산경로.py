def DFS(x, y):
    global count
    if x == endX and y == endY:
        count += 1
    else:
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < n and 0 <= b < n and ch[a][b] == 0 and nList[a][b] > nList[x][y]:
                ch[a][b] = 1
                DFS(a, b)
                ch[a][b] = 0

n = int(input())
nList = [list()]*n

for i in range(n):
    nList[i] = list(map(int, input().split()))

ch=[[0]*n for _ in range(n)]
startX = 0
startY = 0

endX = 0
endY = 0

for i in range(n):
    for j in range(n):
        if nList[i][j] == max(map(max, nList)):
            endX = i
            endY = j
        if nList[i][j] == min(map(min, nList)):
            startX = i
            startY = j

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 0

ch[startX][startY] = 1 #출발점
DFS(startX, startY)
print(count)

