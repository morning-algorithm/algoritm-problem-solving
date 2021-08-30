def DFS(x, y):
    if dy[x][y] > 0:
        return dy[x][y]
    
    if x == 0 and y == 0:
        return nList[0][0]
    else:
        if y == 0:
            dy[x][y] = DFS(x-1, y) + nList[x][y]
        elif x == 0:
            dy[x][y] = DFS(x, y-1) + nList[x][y]
        else: #현재 x,y지점이라면
            dy[x][y] = min(DFS(x-1, y), DFS(x, y-1)) + nList[x][y]
            
        return dy[x][y]

n = int(input())
nList = list()

for i in range(n):
    nList.append(list(map(int, input().split())))

dy=[[0]*n for _ in range(n)]
print(DFS(n-1, n-1))
